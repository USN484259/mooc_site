# Generated by Django 2.2.4 on 2019-08-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20190825_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='source',
            field=models.FileField(upload_to=''),
        ),
    ]
