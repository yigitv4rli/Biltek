# Generated by Django 2.1.7 on 2019-02-23 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20190223_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='articless',
            new_name='article',
        ),
    ]