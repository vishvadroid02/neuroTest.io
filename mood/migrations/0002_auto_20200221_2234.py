# Generated by Django 2.2.5 on 2020-02-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streak_count', models.IntegerField()),
                ('streak_user', models.CharField(max_length=256)),
                ('last_submit', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='mood',
            name='streak_date',
            field=models.DateField(),
        ),
    ]
