# Generated by Django 3.2.4 on 2021-07-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
