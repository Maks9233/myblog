# Generated by Django 5.0.6 on 2024-06-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_article_options_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]
