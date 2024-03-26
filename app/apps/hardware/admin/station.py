from django.contrib import admin

from apps.hardware.models import Station


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass
