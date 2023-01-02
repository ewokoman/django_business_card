# Generated by Django 4.1.4 on 2023-01-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_owner_site_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_site',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
