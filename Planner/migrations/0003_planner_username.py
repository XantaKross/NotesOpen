# Generated by Django 4.1.7 on 2023-04-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planner', '0002_rename_deadline_planner_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='username',
            field=models.CharField(default='AddedBefore', max_length=30),
        ),
    ]