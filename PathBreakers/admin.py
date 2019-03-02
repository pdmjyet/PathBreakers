from django.contrib import admin

from .Models import PathBreaker, Profession

class PathBreakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'yog', 'degree']

class ProfessionTagAdmin(admin.ModelAdmin):
    fields = ['profession', 'tag']
    list_display = ['tag', 'get_professions']

    def get_professions(self, obj):
        return "\n".join([p.name for p in obj.profession.all()])

admin.site.register(PathBreaker.PathBreaker, PathBreakerAdmin)
admin.site.register(Profession.ProfessionTag, ProfessionTagAdmin)
admin.site.register(Profession.Profession)
