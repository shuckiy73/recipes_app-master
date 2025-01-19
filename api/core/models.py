from django.db import models

class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Легко'),
        ('Medium', 'Средне'),
        ('Hard', 'Сложно'),
    )

    CATEGORY_CHOICES = (
        ('Завтрак', 'Завтрак'),
        ('Основное блюдо', 'Основное блюдо'),
        ('Салат', 'Салат'),
        ('Суп', 'Суп'),
        ('Десерт', 'Десерт'),
        ('Закуска', 'Закуска'),
    )

    title = models.CharField(max_length=120, verbose_name='Название рецепта')
    ingredients = models.CharField(max_length=400, verbose_name='Ингредиенты')
    instructions = models.TextField(verbose_name='Инструкция по приготовлению')
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория',
        default='Основное блюдо',  # Значение по умолчанию
        null=True,  # Разрешить NULL в базе данных
        blank=True  # Разрешить пустое значение в формах
    )
    difficulty = models.CharField(
        choices=DIFFICULTY_LEVELS,
        max_length=10,
        verbose_name='Сложность приготовления',
        blank=True,
        null=True
    )
    prep_time = models.PositiveIntegerField(
        verbose_name='Время приготовления (минуты)',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='recipes/',  # Папка для загрузки изображений
        verbose_name='Изображение',
        blank=True,  # Поле необязательное
        null=True  # Разрешить NULL в базе данных
    )

    def __str__(self):
        return "Рецепт: {}".format(self.title)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'