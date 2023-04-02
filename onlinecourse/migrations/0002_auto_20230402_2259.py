# Generated by Django 3.1.3 on 2023-04-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choices',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questions',
            new_name='Course',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_grade',
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='This is a sample question.', max_length=2500),
        ),
    ]