# Generated by Django 4.1.2 on 2022-12-19 19:09

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=400, null=True)),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('social_github', models.CharField(blank=True, max_length=400, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=400, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=400, null=True)),
                ('social_website', models.CharField(blank=True, max_length=400, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
