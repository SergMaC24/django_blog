# Generated by Django 4.1 on 2022-08-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_imageabout_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]