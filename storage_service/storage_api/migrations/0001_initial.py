# Generated by Django 4.2.9 on 2024-01-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('service_name', models.CharField(max_length=200)),
                ('resource_type', models.CharField(max_length=200)),
                ('uuid', models.CharField(max_length=200)),
                ('guid', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=300)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]