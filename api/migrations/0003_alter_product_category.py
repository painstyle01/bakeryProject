# Generated by Django 4.1 on 2022-09-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_categories_alter_discountcodes_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.TextField(choices=[]),
        ),
    ]
