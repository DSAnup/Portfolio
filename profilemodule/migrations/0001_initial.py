# Generated by Django 4.2.8 on 2024-01-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('present_address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
                ('about_me', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='profile')),
                ('title_background', models.ImageField(upload_to='others')),
                ('full_cv', models.FileField(upload_to='cv')),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(choices=[('T1', 'Template one'), ('T2', 'Template Two')], default='T1', max_length=2)),
                ('website_name', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
