# Generated by Django 3.2.4 on 2021-07-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_paymentpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LSHeadingOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
