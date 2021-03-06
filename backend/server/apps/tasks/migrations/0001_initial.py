# Generated by Django 2.1.2 on 2018-10-17 15:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=128)),
                ('params', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('task_id', models.CharField(max_length=128)),
            ],
        ),
    ]
