# Generated by Django 3.2.18 on 2023-04-15 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='grand_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='large_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='small_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
