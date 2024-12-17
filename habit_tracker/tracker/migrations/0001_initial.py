# Generated by Django 5.1.3 on 2024-12-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('progress', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('frequency', models.CharField(max_length=50)),
            ],
        ),
    ]