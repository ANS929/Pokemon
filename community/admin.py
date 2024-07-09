from django.contrib import admin
from .models import MathQuestion, TCGQuestion

admin.site.register(MathQuestion)
admin.site.register(TCGQuestion)