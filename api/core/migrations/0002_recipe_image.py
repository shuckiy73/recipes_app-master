# Generated by Django 5.1.5 on 2025-01-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Изображение'),
        ),
    ]
