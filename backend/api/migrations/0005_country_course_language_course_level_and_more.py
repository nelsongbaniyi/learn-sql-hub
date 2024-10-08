# Generated by Django 4.2 on 2024-01-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_course_user_course_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tax_rate', models.IntegerField(default=5, help_text='Numbers added here are in percentage (5 = 5%)')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], default='English', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=50),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Processing', 'Processing'), ('Failed', 'failed')], default='initiated', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='platform_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Disabled', 'Disabled'), ('Rejected', 'Rejected'), ('In Review', 'In Review'), ('Published', 'Published')], default='published', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Sale Price'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_course_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Disabled', 'Disabled'), ('Published', 'Published')], default='published', max_length=50),
        ),
    ]
