# Generated by Django 3.0.3 on 2020-02-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.FileField(auto_created=True, upload_to='caseFiles')),
                ('accuser_name', models.CharField(max_length=100)),
                ('defendant_name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Solved')], default=0)),
            ],
        ),
    ]