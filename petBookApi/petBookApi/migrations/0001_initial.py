# Generated by Django 2.1.1 on 2018-09-06 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=200)),
                ('side_effects', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_name', models.CharField(max_length=200)),
                ('instructions', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('content', models.CharField(max_length=300)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='%m/%d')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('nick_name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=100)),
                ('houdini', models.BooleanField(default=True)),
                ('food_quirks', models.CharField(max_length=300)),
                ('crate_trained', models.BooleanField(default=True)),
                ('crate_quirks', models.CharField(max_length=300)),
                ('walking_quirks', models.CharField(max_length=300)),
                ('potty_needs', models.CharField(max_length=300)),
                ('aggression_notes', models.CharField(max_length=300)),
                ('eating_times', models.CharField(max_length=300)),
                ('bed_time', models.CharField(max_length=300)),
                ('fav_toy', models.CharField(max_length=300)),
                ('deceased', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PetAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Allergy')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Command')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Note')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='allergy',
            field=models.ManyToManyField(through='petBookApi.PetAllergy', to='petBookApi.Allergy'),
        ),
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Breed'),
        ),
        migrations.AddField(
            model_name='pet',
            name='command',
            field=models.ManyToManyField(through='petBookApi.PetCommand', to='petBookApi.Command'),
        ),
        migrations.AddField(
            model_name='pet',
            name='note',
            field=models.ManyToManyField(through='petBookApi.PetNote', to='petBookApi.Note'),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.PetType'),
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='owner',
            name='follows',
            field=models.ManyToManyField(related_name='follower', through='petBookApi.Follow', to='petBookApi.Pet'),
        ),
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Owner'),
        ),
        migrations.AddField(
            model_name='follow',
            name='pets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Pet'),
        ),
        migrations.AddField(
            model_name='command',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Owner'),
        ),
        migrations.AddField(
            model_name='breed',
            name='pet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.PetType'),
        ),
        migrations.AddField(
            model_name='allergy',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petBookApi.Owner'),
        ),
    ]
