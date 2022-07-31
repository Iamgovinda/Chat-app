import django
from django.contrib import admin
from chat.models import Message,ChatRoom

# # Register your models here.
admin.site.register([Message,ChatRoom])