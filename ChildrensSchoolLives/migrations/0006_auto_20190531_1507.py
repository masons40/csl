# Generated by Django 2.1.5 on 2019-05-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChildrensSchoolLives', '0005_websiteemailaddress_websitephonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitephonenumber',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
