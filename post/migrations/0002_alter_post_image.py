# Generated by Django 4.2.7 on 2023-11-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='defaul.jpg', upload_to=''),
        ),
    ]
