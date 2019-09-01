# Generated by Django 2.2.4 on 2019-08-31 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('course', '0002_auto_20190831_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sorting', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseModel')),
            ],
            options={
                'ordering': ['sorting'],
            },
        ),
        migrations.CreateModel(
            name='ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('score', models.FloatField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.ExamModel')),
                ('selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.SelectionModel')),
            ],
        ),
    ]
