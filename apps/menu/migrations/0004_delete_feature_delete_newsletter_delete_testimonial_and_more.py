# Generated by Django 4.1.4 on 2023-05-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_feature_newsletter_testimonial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Newsletter',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
