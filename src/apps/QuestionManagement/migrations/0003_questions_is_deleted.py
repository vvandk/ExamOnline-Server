# Generated by Django 4.2.8 on 2024-01-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionManagement', '0002_questions_trial_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='是否删除'),
        ),
    ]