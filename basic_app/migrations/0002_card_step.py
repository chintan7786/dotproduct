# Generated by Django 4.1.3 on 2022-11-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="step",
            field=models.CharField(
                blank=True,
                choices=[("TO-DO", "TO-DO"), ("Doing", "Doing"), ("Done", "Done")],
                max_length=50,
                null=True,
            ),
        ),
    ]