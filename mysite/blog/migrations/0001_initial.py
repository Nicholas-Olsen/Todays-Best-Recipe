# Generated by Django 5.1.6 on 2025-02-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                ("rec_id", models.AutoField(primary_key=True, serialize=False)),
                ("rec_name", models.CharField(max_length=200)),
                ("rec_descrip", models.TextField()),
                ("rec_detail", models.TextField()),
                ("rec_img", models.ImageField(upload_to="recipes/")),
                ("rec_type", models.CharField(max_length=100)),
            ],
        ),
    ]
