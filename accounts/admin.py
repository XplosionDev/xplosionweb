from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Team)
class Team_admin(admin.ModelAdmin):
    list_filter = ('state', 'team_name')
@admin.register(models.Player)
class Player_admin(admin.ModelAdmin):
    list_filter = ('team', 'first_name')



admin.site.register(models.Coach)
admin.site.register(models.Swing)