# Generated by Django 2.2.7 on 2020-09-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0011_auto_20200901_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='name',
            field=models.CharField(blank=True, default='No name', help_text='URL name e.g Tinny', max_length=100),
        ),
    ]
