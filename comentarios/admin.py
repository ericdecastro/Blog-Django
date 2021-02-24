from django.contrib import admin
from.models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_comentario',
                    'data_comentario', 'publicado_comentario',)
    list_editable = ('publicado_comentario',)
    list_display_links = ('id',)


admin.site.register(Comentario, ComentarioAdmin)
