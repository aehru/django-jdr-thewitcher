# Generated by Django 4.2.6 on 2023-11-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheWitcher', '0004_recipe_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='investment',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
