from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_student', 'is_teacher')

admin.site.register(Profile, ProfileAdmin)