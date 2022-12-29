# Generated by Django 4.1.3 on 2022-12-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrologerapplogic', '0004_rename_socialname_sociallinks_socialmedianame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blogId', models.AutoField(primary_key=True, serialize=False)),
                ('blogname', models.CharField(max_length=200)),
                ('blogimg', models.FileField(upload_to='uploads/blogimg/')),
                ('blogdesc', models.CharField(max_length=300)),
            ],
        ),
    ]
