# Generated by Django 2.1.2 on 2019-01-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytask',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
