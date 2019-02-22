# Generated by Django 2.1.4 on 2019-02-22 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testpaper', '0001_initial'),
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examstudentsinfo',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.StudentsInfo', verbose_name='考生信息'),
        ),
        migrations.AddField(
            model_name='exampaperinfo',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.ExaminationInfo', verbose_name='考试信息'),
        ),
        migrations.AddField(
            model_name='exampaperinfo',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpaper.TestPaperInfo', verbose_name='试卷信息'),
        ),
        migrations.AddField(
            model_name='examinationinfo',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='examinationinfo',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SubjectInfo', verbose_name='所属科目'),
        ),
    ]
