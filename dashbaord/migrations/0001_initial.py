# Generated by Django 4.2.3 on 2023-07-20 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referal', models.SlugField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank='True', default='', null='True', upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('referal_point', models.IntegerField(default=0)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_type', models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Tron', 'Tron'), ('USDT TRC20', 'USDT TRC20')], max_length=100)),
                ('wallet_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Successful', 'Successful')], default='Pending', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbaord.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_type', models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Tron', 'Tron'), ('USDT TRC20', 'USDT TRC20')], max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Successful', 'Successful')], default='Pending', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashbaord.profile')),
            ],
        ),
    ]
