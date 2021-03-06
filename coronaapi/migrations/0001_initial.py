# Generated by Django 2.2 on 2020-03-19 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoronaComorbidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, max_length=250, null=True, verbose_name='preExistingCondition of patient')),
                ('rate', models.CharField(blank=True, max_length=50, null=True, verbose_name='percentage rate of people sex')),
            ],
        ),
        migrations.CreateModel(
            name='CoronaSex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, max_length=250, null=True, verbose_name='Male or female')),
                ('rate', models.CharField(blank=True, max_length=50, null=True, verbose_name='percentage rate of people sex')),
                ('bysex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bySex', to='coronaapi.CoronaComorbidity')),
            ],
        ),
        migrations.CreateModel(
            name='CoronaAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(blank=True, max_length=250, null=True, verbose_name='Between age of people died')),
                ('rate', models.CharField(blank=True, max_length=50, null=True, verbose_name='percentage rate of people age')),
                ('byage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='byAge', to='coronaapi.CoronaComorbidity')),
            ],
        ),
    ]
