# Generated by Django 2.1.7 on 2019-02-17 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190217_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='topic',
            new_name='category',
        ),
    ]