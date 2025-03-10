# Generated by Django 5.1.6 on 2025-03-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('hazard_rating', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('chemical_type', models.CharField(max_length=50)),
                ('banned_status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
