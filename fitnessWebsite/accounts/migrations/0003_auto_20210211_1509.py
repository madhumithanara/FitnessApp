# Generated by Django 3.1.6 on 2021-02-11 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210211_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='current_height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='goal',
            name='current_weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='goal',
            name='ideal_height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='goal',
            name='ideal_weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_intake', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('calorie_burnt', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('heart_rate', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('hours_slept', models.DecimalField(decimal_places=2, default=1, max_digits=6)),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]