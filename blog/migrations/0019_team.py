# Generated by Django 3.2.4 on 2021-07-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_fheadingfour_fheadingone_fheadingthree_fheadingtwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]