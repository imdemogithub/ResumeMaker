# Generated by Django 3.2.9 on 2021-12-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=12)),
                ('IsActive', models.BooleanField(default=False)),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'master',
            },
        ),
    ]