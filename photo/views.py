    # -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import timezone
from gallery import settings
from photo.forms import ReCaptchaForm
from photo.models import Album, Feedback
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from smtplib import SMTPException


@csrf_protect
def feedback(request):
    print('request GET ' + str(request.path))
    if request.method == 'POST':
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            feed = form.cleaned_data
            try:
                new_feedback = Feedback()
                typed_name = feed['name']
                typed_email = request.POST['email']
                typed_message = request.POST['message']
                typed_subject = request.POST['subject']
            except KeyError:
                return HttpResponseRedirect(reverse('photo:error'))
            else:
                new_feedback.name = typed_name
                new_feedback.email = typed_email
                new_feedback.message = typed_message
                new_feedback.subject = typed_subject
                new_feedback.save()
                print('Saved')
                try:
                    subject = feed['subject']
                    message = typed_name + '\n' + typed_email + '\n' + typed_message + '\n' + typed_subject
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [typed_email]
                    send_mail(subject, message, from_email, to_list, fail_silently=False)
                except SMTPException:
                    return HttpResponseRedirect(reverse('photo:error'))
                else:
                    pass
            return HttpResponseRedirect(reverse('photo:thanks'))
        else:
            return HttpResponseRedirect(reverse('photo:error'))


def thanks(request):
    return render_to_response('photo/thanks.html')


def error(request):
    return render_to_response('photo/error.html')


class IndexView(generic.ListView):
    template_name = 'photo/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Album.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        form = ReCaptchaForm()
        return {'albums': Album.objects.order_by('pub_date'), 'form': form}


'''
# Here's a category-album relation view

class AlbumsView(generic.DetailView):
    model = Category
    template_name = 'photo/albums.html'

    def get_queryset(self):
        """
        Return albums in selected category
        """
        return Category.objects.order_by('name')

    def get_context_data(self, **kwargs):
        form = ReCaptchaForm()
        return {'category': kwargs.get('object'), 'form': form}
'''


class PhotoView(generic.DetailView):
    model = Album
    template_name = 'photo/photos.html'
    def get_queryset(self):
        """
        Return photos in selected album
        """
        return Album.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        form = ReCaptchaForm()
        return {'album': kwargs.get('object'), 'form': form}