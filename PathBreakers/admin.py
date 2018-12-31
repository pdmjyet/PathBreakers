from django.contrib import admin

from .Models import PathBreaker, Profession

#class PathBreakerAdmin(admin.ModelAdmin):

admin.site.register(PathBreaker.PathBreaker)
admin.site.register(Profession.ProfessionTag)
admin.site.register(Profession.Profession)
