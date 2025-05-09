# Generated by Django 5.1.6 on 2025-03-05 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('monthId', models.SmallIntegerField(editable=False)),
                ('dayOfWeek', models.SmallIntegerField(editable=False)),
                ('dayOfMonth', models.SmallIntegerField(editable=False)),
                ('dayOfYear', models.SmallIntegerField(editable=False)),
                ('isWorkingDay', models.BooleanField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='DimPatternGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patternGroupName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DimSymbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbolName', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='DimTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='DimTimeFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeFrameName', models.CharField(max_length=4)),
                ('m1Count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPatternType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patternName', models.CharField(max_length=64)),
                ('patternGroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimpatterngroup')),
            ],
        ),
        migrations.CreateModel(
            name='DimCandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField(editable=False)),
                ('close', models.FloatField(editable=False)),
                ('high', models.FloatField(editable=False)),
                ('low', models.FloatField(editable=False)),
                ('atr16', models.FloatField(blank=True, null=True)),
                ('atrTrex', models.FloatField(blank=True, null=True)),
                ('rsi', models.FloatField(blank=True, null=True)),
                ('candleColor', models.CharField(max_length=1)),
                ('date', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimdate')),
                ('symbol', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimsymbol')),
                ('time', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimtime')),
                ('timeFrame', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimtimeframe')),
            ],
        ),
        migrations.CreateModel(
            name='FactPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endCandle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='endPatterns', to='pattern_bank.dimcandle')),
                ('patternType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pattern_bank.dimpatterntype')),
                ('startCandle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='startPatterns', to='pattern_bank.dimcandle')),
                ('timeFrame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='structTimeFramePatterns', to='pattern_bank.dimtimeframe')),
                ('triggerTimeFrame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='triggerTimeFramePatterns', to='pattern_bank.dimtimeframe')),
            ],
        ),
    ]
