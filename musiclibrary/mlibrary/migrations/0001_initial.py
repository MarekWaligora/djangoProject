# Generated by Django 3.0.2 on 2020-01-29 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albname', models.CharField(max_length=100, verbose_name='Album Name')),
                ('albreleasedate', models.DateTimeField(verbose_name='Relase Date')),
                ('alblabel', models.CharField(max_length=100, verbose_name='Labelled by')),
                ('albtype', models.CharField(max_length=50, verbose_name='carrier type')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(verbose_name='Borrow Date')),
                ('exp_return_date', models.DateTimeField(verbose_name='Expect Return Date')),
                ('return_date', models.DateTimeField(verbose_name='Return Date')),
                ('first_monit_date', models.DateTimeField(verbose_name='1st Monit Date')),
                ('second_monit_date', models.DateTimeField(verbose_name='2nd Monit Date')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mlibrary.Album', verbose_name='Album Id')),
            ],
        ),
        migrations.CreateModel(
            name='MusicKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mkshortdesc', models.CharField(max_length=2, unique=True, verbose_name='Music Kinds short')),
                ('mklongdesc', models.CharField(max_length=20, verbose_name='Music Kind Long descr')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brname', models.CharField(max_length=100, verbose_name='Name')),
                ('brsurname', models.CharField(max_length=100, verbose_name='Surname')),
                ('brmail', models.CharField(max_length=40, verbose_name='Mail')),
                ('brphone', models.CharField(max_length=20, verbose_name='Phone')),
                ('bralbums', models.ManyToManyField(through='mlibrary.Borrow', to='mlibrary.Album')),
            ],
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mlibrary.Borrower', verbose_name='Borrower ID'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artname', models.CharField(max_length=200, unique=True, verbose_name='Artist Name')),
                ('art_est_date', models.DateTimeField(verbose_name='Raise Date')),
                ('artkind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mlibrary.MusicKind', verbose_name='Kind of Music')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='albartist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mlibrary.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='albmusickind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mlibrary.MusicKind', verbose_name='Kind of Music'),
        ),
    ]