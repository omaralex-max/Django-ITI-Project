# Generated by Django 5.1 on 2024-08-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trianee', '0006_alter_trainee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='image',
            field=models.ImageField(blank='True', db_column='Image', null=True, upload_to='trianee/images'),
        ),
    ]
