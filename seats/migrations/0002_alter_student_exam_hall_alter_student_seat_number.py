# Generated by Django 5.2.4 on 2025-07-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_hall',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='seat_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
