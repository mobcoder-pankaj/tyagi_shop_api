# Generated by Django 3.2.7 on 2021-09-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20210912_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='mobile_no',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]