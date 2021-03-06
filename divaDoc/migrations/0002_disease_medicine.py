# Generated by Django 2.1.4 on 2019-01-19 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divaDoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=50)),
                ('dis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set', to='divaDoc.disease')),
            ],
        ),
    ]
