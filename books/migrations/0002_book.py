# Generated by Django 4.0 on 2022-01-03 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('book_url', models.CharField(max_length=150)),
                ('book_image_url', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('favorited_by', models.ManyToManyField(related_name='favorite_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
