# Generated by Django 3.1.2 on 2021-08-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='details',
            field=models.CharField(default='stuff', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='stuff', max_length=100),
            preserve_default=False,
        ),
    ]
