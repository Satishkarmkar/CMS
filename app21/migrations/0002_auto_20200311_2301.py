# Generated by Django 3.0.2 on 2020-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app21', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='uname',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
