# Generated by Django 3.2.4 on 2021-07-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise_info',
            name='zhanghao',
            field=models.CharField(max_length=50, null=True, verbose_name='企业账号'),
        ),
    ]