# Generated by Django 3.2.4 on 2021-07-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_emheadingone_emheadingtwo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emheadingtwo',
            name='image',
        ),
        migrations.AddField(
            model_name='emheadingtwo',
            name='video',
            field=models.FileField(default='Add Your Video Here', upload_to='video/%y'),
        ),
    ]