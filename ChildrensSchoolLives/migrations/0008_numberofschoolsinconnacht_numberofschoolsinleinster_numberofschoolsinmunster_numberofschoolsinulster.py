# Generated by Django 2.1.5 on 2019-05-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChildrensSchoolLives', '0007_newsarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberofSchoolsInConnacht',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_schools', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NumberofSchoolsInLeinster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_schools', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NumberofSchoolsInMunster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_schools', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NumberofSchoolsInUlster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_schools', models.IntegerField()),
            ],
        ),
    ]