# Generated by Django 2.1.7 on 2019-02-23 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20190223_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_article',
            new_name='article',
        ),
    ]
