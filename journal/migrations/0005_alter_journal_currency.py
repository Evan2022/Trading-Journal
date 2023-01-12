# Generated by Django 3.2.16 on 2023-01-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_alter_journal_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='currency',
            field=models.CharField(choices=[('USD', '$'), ('EUR', '€'), ('JPY', '¥'), ('GBP', '£')], max_length=3),
        ),
    ]