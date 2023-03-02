# Generated by Django 4.1.5 on 2023-03-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('leave_start', models.DateTimeField()),
                ('leave_end', models.DateTimeField()),
                ('leave_type', models.CharField(max_length=20)),
                ('reason', models.TextField()),
                ('total_days', models.IntegerField()),
                ('total_left', models.IntegerField()),
            ],
        ),
    ]