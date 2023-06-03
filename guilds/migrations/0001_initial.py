# Generated by Django 4.2.1 on 2023-06-03 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(related_name='guilds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
