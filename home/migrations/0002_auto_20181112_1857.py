# Generated by Django 2.1.3 on 2018-11-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='dataRotateX',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataRotateY',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataRotateZ',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataScale',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataX',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataY',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='slide',
            name='dataZ',
            field=models.IntegerField(),
        ),
    ]
