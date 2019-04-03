# Generated by Django 2.1.3 on 2019-03-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.CharField(max_length=8)),
                ('TMAX', models.FloatField(default=0)),
                ('TMIN', models.FloatField(default=0)),
            ],
            options={
                'ordering': ('DATE',),
            },
        ),
    ]
