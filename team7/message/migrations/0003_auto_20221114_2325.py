# Generated by Django 3.2.16 on 2022-11-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
