# Generated by Django 4.2 on 2024-01-23 18:07

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantitem',
            name='variant_item_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix=''),
        ),
    ]
