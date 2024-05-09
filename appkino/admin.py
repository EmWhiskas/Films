from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ModelActor)
admin.site.register(ModelDirector)
admin.site.register(ModelGenre)
# admin.site.register(ModelOtziv)


class adminPodpiska(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(ModelPodpiska, adminPodpiska)


class adminKino(admin.ModelAdmin):
    list_display = ('name', 'director', 'year', 'podpiska')
    fieldsets = (
        ('О фильме', {
            'fields': ['name', 'info', 'year', 'genre', 'country']
        }),
        ('Люди', {
            'fields': ['actor', 'director']
        }),
        ('Для сайта', {
            'fields': ['poster', 'rating', 'podpiska', 'file']
        })
    )


admin.site.register(ModelKino, adminKino)

class adminOtziv(admin.ModelAdmin):
    list_display = ('user', 'film')

admin.site.register(ModelOtziv, adminOtziv)