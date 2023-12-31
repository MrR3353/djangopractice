# Generated by Django 4.2.3 on 2023-07-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat_id', models.CharField(max_length=200, verbose_name='Чат id')),
                ('tg_message', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Настройка телеграмм',
                'verbose_name_plural': 'Настройки телеграмм',
            },
        ),
    ]
