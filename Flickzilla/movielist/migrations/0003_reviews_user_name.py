# Generated by Django 4.1.1 on 2022-09-22 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movielist', '0002_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='user_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
