# Generated by Django 4.1.3 on 2023-01-09 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.2.png', null=True, upload_to=''),
        ),
    ]
