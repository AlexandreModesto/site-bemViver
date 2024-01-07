from django.contrib import admin
from .models import Key_Panel

class ListFamily(admin.ModelAdmin):
    list_display = ('id','resident','check_in','check_out')

admin.site.register(Key_Panel,ListFamily)

