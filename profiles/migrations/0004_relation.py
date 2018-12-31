# Generated by Django 2.1.1 on 2018-12-25 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20181220_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(choices=[('MO', 'Mother'), ('FA', 'Father'), ('SI', 'Sister'), ('BR', 'Brother'), ('DA', 'Daughter'), ('SO', 'Son')], max_length=2)),
                ('from_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_relation', to='profiles.UserProfile')),
                ('to_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_with', to='profiles.UserProfile')),
            ],
        ),
    ]
