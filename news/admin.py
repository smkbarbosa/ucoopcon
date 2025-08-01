from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from .models import Noticia as News,  Categoria as NewsCategory


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'conteudo', 'categoria', 'status', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('categoria', 'status')
    date_hierarchy = 'data_publicacao'
   # prepopulated_fields = {'slug': ('titulo',)}


@admin.register(NewsCategory)
class NewsCategoryAdmin(ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    #prepopulated_fields = {'slug': ('nome',)}


    