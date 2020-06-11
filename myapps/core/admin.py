from django.contrib import admin
from .models import Color


# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Color, ColorAdmin)
admin.site.site_header = 'Haritha Computers & Technology'
