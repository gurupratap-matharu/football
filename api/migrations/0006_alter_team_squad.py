# Generated by Django 4.1.7 on 2023-02-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_coach_date_of_birth_alter_coach_nationality_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="squad",
            field=models.ManyToManyField(related_name="current_teams", to="api.player"),
        ),
    ]