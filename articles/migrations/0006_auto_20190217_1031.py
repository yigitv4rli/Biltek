# Generated by Django 2.1.7 on 2019-02-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20190217_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.TextField(default='Güncel'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
