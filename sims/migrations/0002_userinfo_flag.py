# Generated by Django 3.2.4 on 2021-06-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='flag',
            field=models.CharField(default=0, max_length=20, verbose_name='标志'),
            preserve_default=False,
        ),
    ]