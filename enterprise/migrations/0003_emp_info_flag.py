# Generated by Django 3.2.4 on 2021-07-16 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_enterprise_info_zhanghao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_info',
            name='flag',
            field=models.CharField(default=0, max_length=20, verbose_name='标志'),
        ),
    ]
