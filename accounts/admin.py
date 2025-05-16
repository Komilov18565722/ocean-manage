from django.contrib import admin
from . import models, forms

class UserAdmin(admin.ModelAdmin):
    form = forms.UserForm
    list_display = ['username', 'phone_number', 'email', 'first_name', 'type']
    list_filter = ['username', 'phone_number', 'first_name', 'last_name']
    search_fields = ['username', 'phone_number', 'first_name', 'last_name', 'email']
    
    
admin.site.register(models.User, UserAdmin)

admin.site.register(models.Job)