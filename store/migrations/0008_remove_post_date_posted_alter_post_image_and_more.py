# Generated by Django 5.1.dev20240306045047 on 2024-03-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
