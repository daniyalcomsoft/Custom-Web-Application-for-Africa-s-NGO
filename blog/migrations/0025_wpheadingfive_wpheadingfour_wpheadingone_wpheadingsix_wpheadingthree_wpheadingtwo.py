# Generated by Django 3.2.4 on 2021-07-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20210704_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='WPHeadingFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WPHeadingFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WPHeadingOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WPHeadingSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WPHeadingThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WPHeadingTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
