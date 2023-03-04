# Generated by Django 4.1.5 on 2023-02-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='stype',
            field=models.BooleanField(default=False),
        ),
    ]
