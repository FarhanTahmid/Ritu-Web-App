# Generated by Django 4.0.5 on 2022-09-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0037_alter_players_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketplace',
            name='id',
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='product_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Name'),
        ),
    ]
