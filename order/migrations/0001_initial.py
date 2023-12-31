# Generated by Django 4.2.1 on 2023-06-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('order_total', models.FloatField()),
                ('customer', models.TextField()),
                ('date', models.DateField()),
                ('products', models.TextField()),
                ('delivery_date', models.DateField()),
                ('payment_options', models.CharField(max_length=20)),
            ],
        ),
    ]
