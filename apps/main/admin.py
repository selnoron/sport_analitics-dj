from django.contrib import admin
from .models import Sports, Matches, Favourite


class SportsAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'name',
    )
    list_filter: list[str] = (
        'name',
    )

class MatchesAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'sport_type',
    )
    list_filter: list[str] = (
        'sport_type',
    )

class FavouritesAdmin(admin.ModelAdmin):
    list_display:list[str] = (
        'user',
    )
    list_filter: list[str] = (
        'id',
    )


admin.site.register(Sports, SportsAdmin)
admin.site.register(Matches, MatchesAdmin)
admin.site.register(Favourite, FavouritesAdmin)