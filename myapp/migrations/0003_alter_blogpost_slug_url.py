# Generated by Django 4.2 on 2023-04-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_topic_blogpost_topics_rename_user_topic_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug_url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]