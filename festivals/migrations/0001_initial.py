# Generated by Django 2.1.7 on 2019-03-10 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=510)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=510)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FestivalShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivals.Artist')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivals.Festival')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=510)),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festivals.Festival')),
            ],
        ),
    ]
