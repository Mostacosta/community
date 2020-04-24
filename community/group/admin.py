from django.contrib import admin
from .models import groups,posts,comments

# Register your models here.

admin.site.register(groups)
admin.site.register(posts)
admin.site.register(comments)