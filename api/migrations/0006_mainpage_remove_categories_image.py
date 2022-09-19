# Generated by Django 4.1 on 2022-09-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_delete_menubar'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pic', models.ImageField(upload_to='main_page')),
            ],
        ),
        migrations.RemoveField(
            model_name='categories',
            name='image',
        ),
    ]
