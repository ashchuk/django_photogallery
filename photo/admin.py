# coding=utf-8
from django.contrib import admin
from photo.models import Album, Photo, Feedback
# Register your models here.


class PhotoInLine(admin.TabularInline):
    model = Photo
    extra = 10


class AlbumsInLine(admin.TabularInline):
    model = Album
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Album thumbnail', {'fields': ['album_thumbnail']}),
    ]
    inlines = [PhotoInLine]
    list_display = ('name', 'pub_date', 'description')
    list_filter = ['pub_date']
    search_fields = ['name']

'''
class CategoryAdmin(admin.ModelAdmin):
    inlines = [AlbumsInLine]

# And add 'category' in fieldsets and list_display
'''


class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'message', 'email', 'subject']}),
    ]
    list_display = ('name', 'pub_date', 'message', 'email', 'subject')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)
