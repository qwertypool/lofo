# Generated by Django 3.0.4 on 2020-04-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=150)),
                ('clocation', models.CharField(max_length=150)),
            ],
        ),
    ]
