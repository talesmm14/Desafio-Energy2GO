from django.contrib import admin

from apps.hardware.models import Batery


@admin.register(Batery)
class BateryAdmin(admin.ModelAdmin):
    pass
