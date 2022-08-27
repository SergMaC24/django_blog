from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'post')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_at', 'id')
    inlines = [RecipeInline]
    """copy post"""
    save_as = True
    """button on top"""
    save_on_top = True

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Comment)
