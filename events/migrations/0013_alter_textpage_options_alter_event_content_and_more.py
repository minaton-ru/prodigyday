# Generated by Django 4.1.7 on 2023-08-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_remove_textpage_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textpage',
            options={'ordering': ['slug']},
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]