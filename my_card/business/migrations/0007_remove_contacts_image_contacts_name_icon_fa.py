# Generated by Django 4.1.4 on 2023-01-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_projects_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='image',
        ),
        migrations.AddField(
            model_name='contacts',
            name='name_icon_fa',
            field=models.CharField(default='fa-regular fa-envelope', max_length=100),
        ),
    ]
