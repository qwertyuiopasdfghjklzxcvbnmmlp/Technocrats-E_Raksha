# Generated by Django 4.0.3 on 2023-07-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='b_descp',
            field=models.TextField(null=True),
        ),
    ]
