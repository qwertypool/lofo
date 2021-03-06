# Generated by Django 3.0.4 on 2020-04-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='found',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lost',
            name='details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='found',
            name='card',
            field=models.CharField(default='Adhar Card', max_length=50),
        ),
        migrations.AlterField(
            model_name='lost',
            name='card',
            field=models.CharField(default='Adhar Card', max_length=50),
        ),
    ]
