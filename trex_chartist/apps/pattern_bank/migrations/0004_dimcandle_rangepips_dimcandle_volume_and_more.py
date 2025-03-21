# Generated by Django 5.1.6 on 2025-03-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern_bank', '0003_alter_dimdate_dayofmonth_alter_dimdate_dayofweek_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimcandle',
            name='rangePips',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimcandle',
            name='volume',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dimcandle',
            name='candleColor',
            field=models.CharField(choices=[('g', 'green'), ('e', 'equal'), ('r', 'red')], max_length=1),
        ),
    ]
