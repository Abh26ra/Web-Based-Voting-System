# Generated by Django 3.1.7 on 2021-04-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbvs', '0014_remove_history_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='allowed',
            field=models.IntegerField(default=0),
        ),
    ]
