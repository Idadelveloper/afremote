# Generated by Django 4.2.5 on 2023-09-26 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_skills_interest"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="skills",
            name="user",
        ),
        migrations.DeleteModel(
            name="Interest",
        ),
        migrations.DeleteModel(
            name="Skills",
        ),
    ]
