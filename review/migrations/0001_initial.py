# Generated by Django 4.2.1 on 2023-06-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=32)),
                ('products', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
