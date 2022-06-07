# Generated by Django 4.0 on 2022-06-07 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('followings', models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ImageField(upload_to='migram/story')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migram.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reel', models.FileField(upload_to='migram/reel')),
                ('likes', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='migram/photos')),
                ('caption', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='migram.profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
