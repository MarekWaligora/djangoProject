# Generated by Django 3.0.2 on 2020-02-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlibrary', '0002_auto_20200201_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='art_est_date',
            field=models.DateField(verbose_name='Raise Date'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='exp_return_date',
            field=models.DateField(null=True, verbose_name='Expect Return Date'),
        ),
    ]
