# Generated by Django 2.2.4 on 2020-08-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rjjewellers', '0002_auto_20200806_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldimage',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goldimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
