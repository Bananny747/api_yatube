# Generated by Django 3.2 on 2023-02-20 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_unique_text_author'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='post',
            name='unique_text_author',
        ),
    ]
