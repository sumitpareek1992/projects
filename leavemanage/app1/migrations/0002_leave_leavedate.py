# Generated by Django 2.1.5 on 2019-05-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='leavedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
