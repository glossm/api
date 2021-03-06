# Generated by Django 2.0.4 on 2018-04-13 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcription', '0002_auto_20180405_1050'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='record',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='record',
            name='language',
        ),
        migrations.RemoveField(
            model_name='record',
            name='meaning',
        ),
        migrations.AlterField(
            model_name='submission',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submissions', to='core.Record'),
        ),
        migrations.AlterModelTable(
            name='submission',
            table='Submission',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Meaning',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
