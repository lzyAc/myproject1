# Generated by Django 5.1.4 on 2024-12-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True, verbose_name='Task name')),
                ('status', models.CharField(choices=[('u', 'Not started yet'), ('o', 'Ongoing'), ('f', 'Finished')], max_length=1, verbose_name='Task status')),
            ],
        ),
    ]
