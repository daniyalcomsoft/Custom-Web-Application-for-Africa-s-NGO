# Generated by Django 3.2.4 on 2021-07-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_indexofsecondheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexOfThirdHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
