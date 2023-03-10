# Generated by Django 4.1.7 on 2023-02-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0012_alter_team_tla"),
    ]

    operations = [
        migrations.AlterField(
            model_name="area",
            name="code",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="coach",
            name="name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="player",
            name="name",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
