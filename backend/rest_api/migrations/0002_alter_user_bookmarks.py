# Generated by Django 4.0.6 on 2022-07-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='users', to='rest_api.notice'),
        ),
    ]