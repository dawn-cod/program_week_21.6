# Generated by Django 3.2.4 on 2021-06-14 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentinfo',
            name='basicinfo',
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='tv_name',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='firstWeb.basicinfo'),
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentinfo',
            name='overall',
            field=models.CharField(max_length=999),
        ),
    ]
