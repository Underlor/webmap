from django.contrib import admin

# Register your models here.
from pcinfo.models import PC


@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    pass