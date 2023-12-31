# Generated by Django 4.2.3 on 2023-07-20 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbaord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposite',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='amount',
            field=models.FloatField(),
        ),
    ]
