# Generated by Django 2.1.1 on 2018-10-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_notice_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='numbers',
            field=models.IntegerField(default=1),
        ),
    ]
