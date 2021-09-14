from django.contrib import admin
from posts.models import Post

# Enviando al administrador que registre el modelo Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']