# Generated by Django 2.2 on 2020-03-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coronaapi', '0005_auto_20200320_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Latitude of country')),
                ('long', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Longitude of country')),
                ('country', models.CharField(blank=True, max_length=250, null=True, verbose_name='Country name')),
                ('country_code', models.CharField(blank=True, max_length=250, null=True, verbose_name='Country code name')),
                ('totalConfirmed', models.IntegerField(blank=True, null=True, verbose_name='Total confirm cases in country')),
                ('totalDeaths', models.IntegerField(blank=True, null=True, verbose_name='Total death cases in country')),
                ('totalRecovered', models.IntegerField(blank=True, null=True, verbose_name='Total recovered cases in country')),
                ('province', models.CharField(blank=True, max_length=250, null=True, verbose_name='Country state name')),
            ],
        ),
    ]
