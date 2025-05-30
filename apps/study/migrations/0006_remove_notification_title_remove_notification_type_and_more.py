# Generated by Django 5.0.2 on 2025-05-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_alter_studyprogress_last_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='title',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('goal', '학습 목표 달성'), ('streak', '연속 학습 달성'), ('mastery', '단어 완벽 암기'), ('level', '레벨 달성'), ('friend', '친구 관련')], default='goal', max_length=20),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
