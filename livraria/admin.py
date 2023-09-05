from django.contrib import admin

from .models import Autor, Categoria, Editora, Localização, Livro, Usuario, Carrinho

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Localização)
admin.site.register(Livro)
admin.site.register(Usuario)
admin.site.register(Carrinho)
