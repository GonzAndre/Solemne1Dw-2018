from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'age', 'height', 'weight', 'thumb', )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))

@admin.register(Coach)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'age','email','nickname',)
    
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('local','visit', 'date',)
    
@admin.register(Roster)    
class RosterAdmin(admin.ModelAdmin):
    pass
    
@admin.register(RosterMatch)
class RosterMatchAdmin(admin.ModelAdmin):
    pass

@admin.register(InterRoster)
class InterRosterAdmin(admin.ModelAdmin):
    pass