# Generated by Django 5.2 on 2025-05-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
