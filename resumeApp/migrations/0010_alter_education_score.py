# Generated by Django 3.2.9 on 2022-01-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0009_alter_education_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Score',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True, verbose_name=0),
        ),
    ]
