# Generated by Django 4.1.5 on 2023-02-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='picture',
            field=models.ImageField(null=True, upload_to='patient_pictures/'),
        ),
    ]