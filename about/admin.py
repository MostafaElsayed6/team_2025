from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = ('name', 'role')

admin.site.site_header="صفحة ادارة  الموقع"
admin.site.site_title="kma"