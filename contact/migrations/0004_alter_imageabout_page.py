# Generated by Django 4.1 on 2022-08-17 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_social_imageabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageabout',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_images', to='contact.about'),
        ),
    ]