# Generated by Django 2.1.5 on 2019-05-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChildrensSchoolLives', '0006_auto_20190531_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('news_article_company', models.CharField(max_length=400)),
                ('news_article_url', models.URLField(max_length=500)),
            ],
        ),
    ]
