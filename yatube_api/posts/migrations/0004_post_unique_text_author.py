# Generated by Django 3.2 on 2023-02-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_unique_text_author'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='post',
            constraint=models.UniqueConstraint(fields=('text', 'author'), name='unique_text_author'),
        ),
    ]
