# Generated by Django 3.2.4 on 2021-07-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_wpheadingfive_wpheadingfour_wpheadingone_wpheadingsix_wpheadingthree_wpheadingtwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MDHeadingOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MDHeadingThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MDHeadingTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
