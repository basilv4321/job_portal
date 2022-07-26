# Generated by Django 4.0.3 on 2022-07-23 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'applied'), ('rejected', 'rejected'), ('pending', 'pending'), ('cancelled', 'cancelled'), ('accepted', 'accepted')], default='applied', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aapplicants', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ajobs', to='employers.jobs')),
            ],
        ),
        migrations.DeleteModel(
            name='Applications',
        ),
    ]
