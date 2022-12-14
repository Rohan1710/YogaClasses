# Generated by Django 3.2.16 on 2022-12-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('age', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=22)),
                ('address', models.CharField(max_length=144)),
                ('payment_status', models.BooleanField()),
                ('batch', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
