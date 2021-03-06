# Generated by Django 3.1.3 on 2020-11-23 18:47

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='serie',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='serie',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('flag', models.CharField(blank=True, max_length=2, null=True)),
                ('union', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='coins.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
