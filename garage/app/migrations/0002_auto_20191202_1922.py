# Generated by Django 2.0.4 on 2019-12-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='second_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='second name of customer'),
        ),
    ]