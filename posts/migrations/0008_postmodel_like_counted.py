# Generated by Django 3.2 on 2021-04-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_postmodel_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='like_counted',
            field=models.PositiveIntegerField(default=0),
        ),
    ]