# Generated by Django 2.2.7 on 2020-02-11 18:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coplay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('credit', models.PositiveIntegerField(default=0)),
                ('total_earn', models.PositiveIntegerField(default=0)),
                ('total_spent', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('item_price', models.IntegerField(default=0)),
                ('number_of_items', models.PositiveIntegerField(default=1)),
                ('total_price', models.IntegerField(default=0)),
                ('credit', models.IntegerField(default=0)),
                ('url', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='url')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='שם החנות')),
                ('currency_name', models.CharField(default='MemeCache', max_length=200, verbose_name='שם המטבע')),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(2000)], verbose_name='תאור')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('segment', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='coplay.Segment')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='שם המוצר')),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(2000)], verbose_name='תאור')),
                ('item_price', models.PositiveIntegerField(default=0, verbose_name='מחיר')),
                ('number_of_abailabale_items', models.PositiveIntegerField(default=0, verbose_name='כמה במלאי')),
                ('number_of_selected_items', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('end_of_sale_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='סיום המכירה')),
                ('end_of_use_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='תקף עד')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='memecache.Product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Purchase')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Shop')),
            ],
            options={
                'unique_together': {('shop', 'customer')},
            },
        ),
        migrations.CreateModel(
            name='ProductSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_selected_items', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memecache.Product')),
            ],
            options={
                'unique_together': {('product', 'cart')},
            },
        ),
    ]
