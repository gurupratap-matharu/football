from django.contrib import admin

from .models import Area, Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "area")


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name",)
