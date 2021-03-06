# Generated by Django 3.2.6 on 2021-08-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoblog', '0003_remove_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='desc',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='userid',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
