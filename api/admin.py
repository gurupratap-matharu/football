from django.contrib import admin

from .models import Area, Coach, Competition, Player, Team

admin.site.site_header = "Football ⚽️"
admin.site.site_title = "Football API Admin Portal"
admin.site.index_title = "Welcome to Football Admin Portal"


class TeamInline(admin.TabularInline):
    model = Competition.teams.through
    extra = 0
    can_delete = False


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "area")
    exclude = ("teams",)
    inlines = [TeamInline]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "tla", "short_name", "address", "area")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "date_of_birth", "nationality")


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "nationality", "team")
