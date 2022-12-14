# Generated by Django 4.1 on 2022-08-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NftRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('max_supply', models.IntegerField()),
                ('nbr_minted', models.IntegerField()),
                ('nbr_of_holders', models.IntegerField()),
                ('total_number_of_followers', models.IntegerField()),
            ],
        ),
    ]
