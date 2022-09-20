# Generated by Django 4.1 on 2022-09-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_mainpage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('cart', models.TextField()),
                ('contact_phone', models.TextField()),
                ('email', models.TextField()),
                ('delivery_type', models.TextField()),
                ('messanger', models.TextField()),
                ('payment_type', models.TextField()),
            ],
        ),
    ]
