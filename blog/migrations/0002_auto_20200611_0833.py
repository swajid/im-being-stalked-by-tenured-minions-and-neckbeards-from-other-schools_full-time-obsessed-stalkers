# Generated by Django 3.0.6 on 2020-06-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='hello', max_length=40),
            preserve_default=False,
        ),
    ]
