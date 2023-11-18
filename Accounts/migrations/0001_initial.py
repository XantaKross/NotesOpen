# Generated by Django 4.1.7 on 2023-04-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]