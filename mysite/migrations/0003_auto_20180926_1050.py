# Generated by Django 2.0.2 on 2018-09-26 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180926_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogarticles',
            name='author',
        ),
        migrations.DeleteModel(
            name='BlogArticles',
        ),
    ]
