# Generated by Django 5.0.6 on 2024-06-19 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('id',), 'verbose_name': 'Проданный товар', 'verbose_name_plural': 'Проданные товары'},
        ),
    ]
