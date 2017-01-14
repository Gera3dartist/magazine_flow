from django.contrib import admin
from moderator.models import Moderator


class ModeratorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Moderator, ModeratorAdmin)
