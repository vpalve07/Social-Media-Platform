# Generated by Django 4.1.1 on 2022-09-29 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_commentpost_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentPost',
        ),
    ]
