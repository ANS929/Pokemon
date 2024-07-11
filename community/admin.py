from django.contrib import admin
from .models import MathQuestion, TCGQuestion, MathComment, TCGComment

admin.site.register(MathQuestion)
admin.site.register(TCGQuestion)
admin.site.register(MathComment)
admin.site.register(TCGComment)