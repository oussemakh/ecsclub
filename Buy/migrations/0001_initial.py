# Generated by Django 2.1 on 2018-10-20 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='by',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('cin', models.IntegerField()),
                ('address', models.CharField(default=' city  street house_number', max_length=250)),
                ('date', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.PROD')),
            ],
        ),
    ]