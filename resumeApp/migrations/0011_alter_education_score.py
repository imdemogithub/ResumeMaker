# Generated by Django 3.2.9 on 2022-01-07 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0010_alter_education_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Score',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
