# Generated by Django 3.2.6 on 2021-08-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]