# Generated by Django 4.1 on 2022-11-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_user_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="user",
            name="photo",
            field=models.ImageField(null=True, upload_to="users"),
        ),
        migrations.DeleteModel(
            name="profile",
        ),
    ]
