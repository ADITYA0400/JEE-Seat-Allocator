# Generated by Django 3.0a1 on 2020-04-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0007_candidate_locked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
