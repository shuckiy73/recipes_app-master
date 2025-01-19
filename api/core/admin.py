from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'prep_time', 'difficulty')  # Убедитесь, что поля существуют в модели
    search_fields = ('title', 'ingredients')  # Поля для поиска
    list_filter = ('category', 'difficulty')  # Поля для фильтрации