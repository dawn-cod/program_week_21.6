# Generated by Django 3.2.4 on 2021-06-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstWeb', '0004_alter_commentinfo_basicinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='year',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]
