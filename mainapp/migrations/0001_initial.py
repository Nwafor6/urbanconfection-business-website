# Generated by Django 3.2.9 on 2022-06-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('img', models.FileField(upload_to='')),
                ('category', models.CharField(choices=[('wedding Cake', 'Wedding Cake'), ('wedding Cake', 'Wedding Cake')], max_length=100)),
            ],
        ),
    ]