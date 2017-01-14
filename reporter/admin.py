from django.contrib import admin
from reporter.models import Reporter


class ReporterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reporter, ReporterAdmin)
