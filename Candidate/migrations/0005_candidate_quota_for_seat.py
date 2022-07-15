# Generated by Django 3.0.4 on 2020-03-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0004_auto_20200323_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='quota_for_seat',
            field=models.CharField(blank=True, choices=[('GEN', 'GEN'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('GENPWD', 'GENPWD'), ('OBCPWD', 'OBCPWD'), ('SCPWD', 'SCPWD'), ('STPWD', 'STPWD')], max_length=100),
        ),
    ]
