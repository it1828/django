# Generated by Django 3.2 on 2021-04-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=40, verbose_name='Band name')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('est_date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='Establishing date')),
            ],
            options={
                'ordering': ['band_name'],
            },
        ),
    ]
