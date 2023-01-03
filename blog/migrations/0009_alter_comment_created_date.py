# Generated by Django 4.1.3 on 2022-12-01 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_comment_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Одобрен?"
            ),
        ),
    ]