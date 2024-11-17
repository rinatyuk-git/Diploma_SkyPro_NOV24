# Generated by Django 5.1.2 on 2024-11-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_document_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Approved'), ('d', 'Declined')], max_length=1, null=True, verbose_name='Document approving mark'),
        ),
    ]