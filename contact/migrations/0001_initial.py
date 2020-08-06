# Generated by Django 3.0.2 on 2020-07-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
