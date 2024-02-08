# Generated by Django 4.2.6 on 2024-01-11 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlchemicalSubstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('vitriol', 'Vitriol'), ('rebis', 'Rebis'), ('caelum', 'Caelum'), ('hydragenum', 'Hydragenum'), ('vermillion', 'Vermillion'), ('sol', 'Sol'), ('fulgur', 'Fulgur'), ('aether', 'Aether'), ('quebrith', 'Quebrith')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AlchemyRecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(blank=True, max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('money', models.FloatField(default=0)),
                ('xp', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tag', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('difficulty', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('weight', models.FloatField()),
                ('location', models.CharField(max_length=80)),
                ('category', models.CharField(choices=[('alchemy_ingredient', 'Alchemy Ingredient'), ('craft_material', 'Craft Material'), ('animals', 'Animals'), ('alchemy_treatment', 'Alchemy Treatment'), ('minerals', 'Minerals')], max_length=20)),
                ('substance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.alchemicalsubstance')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('level', models.CharField(choices=[('novice', 'Novice'), ('journeyman', 'Journeyman'), ('master', 'Master'), ('grandmaster', 'Grandmaster')], max_length=20)),
                ('difficulty', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('investment', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('formula', 'Alchemy'), ('ingredient', 'Ingredient'), ('armor', 'Armor'), ('weapon', 'Weapon')], max_length=20)),
                ('item_crafted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_crafted_by_recipe', to='TheWitcher.item')),
            ],
        ),
        migrations.CreateModel(
            name='AlchemyRecipe',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TheWitcher.recipe')),
            ],
            bases=('TheWitcher.recipe',),
        ),
        migrations.CreateModel(
            name='CraftRecipe',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TheWitcher.recipe')),
            ],
            bases=('TheWitcher.recipe',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('characteristic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.characteristic')),
            ],
        ),
        migrations.CreateModel(
            name='CraftRecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.item')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.character')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.skill')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.character')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.character')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.item')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.character')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheWitcher.characteristic')),
            ],
        ),
    ]
