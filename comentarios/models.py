from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.utils import timezone


class Comentario(models.Model):

    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    comentario = models.TextField()
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário', blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=True, verbose_name='Publicado')

    def __str__(self):
        return self.usuario_comentario
