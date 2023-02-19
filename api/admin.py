from django.contrib import admin

from .models import Area, Competition, Player, Team


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "area")


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "tla", "short_name", "address", "area")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "date_of_birth", "nationality")
