# Generated by Django 4.1.7 on 2023-04-04 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hero_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('hero_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.details')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='movie_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.movie'),
        ),
    ]