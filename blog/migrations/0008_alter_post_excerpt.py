# Generated by Django 4.0.3 on 2022-08-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=200, null=True),
        ),
    ]