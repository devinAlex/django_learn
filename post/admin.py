from django.contrib import admin

# Register your models here.
from post.models import *
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','category']
    list_filter = ['category']

admin.site.register(Category)
admin.site.register(Post,PostModelAdmin)
