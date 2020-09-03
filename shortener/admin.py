from django.contrib import admin
from .models import User, URLShortener, Record
# Register your models here.

admin.site.register(User)
admin.site.register(URLShortener)
admin.site.register(Record)