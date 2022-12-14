# Generated by Django 4.1.1 on 2022-09-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_surveyparticipant_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='survey.question'),
        ),
    ]
