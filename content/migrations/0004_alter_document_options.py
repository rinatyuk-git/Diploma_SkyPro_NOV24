# Generated by Django 5.1.2 on 2024-11-11 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_document_is_approved_document_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
    ]
