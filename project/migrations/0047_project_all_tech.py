# Generated by Django 3.2.7 on 2021-10-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0046_issue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='all_tech',
            field=models.CharField(blank=True, max_length=112, null=True),
        ),
    ]
