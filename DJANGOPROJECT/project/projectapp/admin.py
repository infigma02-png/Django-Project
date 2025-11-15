from django.contrib import admin
from .models import Users

@admin.register(Users)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Firstname', 'Lastname', 'Email', 'Subject', 'Message')
