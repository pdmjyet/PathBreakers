from django.contrib import admin

from .Models import PathBreaker, Profession


#class professionInline(admin.TabularInline):
#    model = Profession.ProfessionTag.profession.through

#class professionTagInline(admin.TabularInline):
#    model = PathBreaker.PathBreaker.professionTag.through


class PathBreakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'yog', 'degree']
    #inlines = [
    #                professionTagInline,
    #           ]
    #exclude = ('professionTag',)


class ProfessionTagAdmin(admin.ModelAdmin):
    fields = ['profession', 'tag']
    list_display = ['tag', 'profession']

    def get_professions(self, obj):
        return "\n".join([p.name for p in obj.profession.all()])

admin.site.register(PathBreaker.PathBreaker, PathBreakerAdmin)
admin.site.register(Profession.ProfessionTag, ProfessionTagAdmin)
admin.site.register(Profession.Profession)
admin.site.register(Profession.Tag)
