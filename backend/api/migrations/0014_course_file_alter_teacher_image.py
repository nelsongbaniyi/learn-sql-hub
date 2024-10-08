# Generated by Django 4.2 on 2024-01-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_teacher_facebook_teacher_linkedin_teacher_twitter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='course-file'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='course-file'),
        ),
    ]
