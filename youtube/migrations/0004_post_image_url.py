# Generated by Django 4.2.3 on 2023-07-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
