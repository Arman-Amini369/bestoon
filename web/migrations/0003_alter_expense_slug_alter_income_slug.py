# Generated by Django 5.0 on 2023-12-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_expense_slug_alter_income_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
