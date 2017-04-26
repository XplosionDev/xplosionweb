from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Teams)
class Team_admin(admin.ModelAdmin):
    list_filter = ('state', 'team_name')
@admin.register(models.Players)
class Player_admin(admin.ModelAdmin):
    list_filter = ('team', 'first_name')



admin.site.register(models.Coachs)
admin.site.register(models.Swings)