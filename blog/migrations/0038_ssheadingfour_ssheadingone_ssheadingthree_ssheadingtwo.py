# Generated by Django 3.2.4 on 2021-07-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_wsbottomimage_wsheadingone_wstopimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSHeadingFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SSHeadingOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='video/%y')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SSHeadingThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description1', models.CharField(max_length=1000)),
                ('description2', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SSHeadingTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
