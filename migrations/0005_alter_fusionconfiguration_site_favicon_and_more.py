# Generated by Django 4.2.3 on 2023-08-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0004_fusionconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fusionconfiguration',
            name='site_favicon',
            field=models.ImageField(upload_to='fusion/static/img/site/img'),
        ),
        migrations.AlterField(
            model_name='fusionconfiguration',
            name='site_icon',
            field=models.ImageField(upload_to='fusion/static/img/site/img'),
        ),
    ]
