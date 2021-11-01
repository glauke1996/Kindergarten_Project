# Generated by Django 3.2.5 on 2021-10-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]