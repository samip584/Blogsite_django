# Generated by Django 2.2.2 on 2019-06-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='sluggg'),
            preserve_default=False,
        ),
    ]
