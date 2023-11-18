# Generated by Django 4.1.7 on 2023-03-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('Priority', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('Task', models.CharField(max_length=300)),
                ('Add_On', models.DateTimeField(auto_now_add=True)),
                ('DeadLine', models.DateTimeField()),
            ],
        ),
    ]
