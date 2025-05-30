# Generated by Django 5.0.2 on 2025-05-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_userprofile_last_level_up_date_userprofile_points_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_level_up_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_study_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='points_to_next_level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='streak_days',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='total_studied_words',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='daily_goal',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dark_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
