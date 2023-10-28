# Generated by Django 4.2.6 on 2023-10-27 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0003_alter_video_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to=settings.AUTH_USER_MODEL),
        ),
    ]