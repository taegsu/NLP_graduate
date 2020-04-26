# Generated by Django 2.2 on 2019-05-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_mention_keyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musinsa_Mention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='DEFAULT VALUE', max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('mentions', models.BigIntegerField()),
                ('reviews', models.BigIntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Mention',
            new_name='Instagram_Mention',
        ),
    ]
