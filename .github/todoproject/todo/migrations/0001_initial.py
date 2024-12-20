# Generated by Django 5.1.3 on 2024-12-20 08:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]