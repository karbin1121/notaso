# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 01:26
from __future__ import unicode_literals

import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import autoslug.fields
import notaso.professors.models


class Migration(migrations.Migration):

    replaces = [
        (b"professors", "0001_initial"),
        (b"professors", "0002_auto_20180825_2204"),
    ]

    initial = True

    dependencies = [
        ("departments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("universities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=75)),
                (
                    "gender",
                    models.CharField(
                        choices=[(b"M", b"Male"), (b"F", b"Female")], max_length=1
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from=notaso.professors.models.populate_professor_slug,
                        unique=True,
                    ),
                ),
                ("score", models.FloatField(default=0, editable=False)),
                ("responsibility", models.FloatField(default=0, editable=False)),
                ("personality", models.FloatField(default=0, editable=False)),
                ("workload", models.FloatField(default=0, editable=False)),
                ("difficulty", models.FloatField(default=0, editable=False)),
                (
                    "search_index",
                    django.contrib.postgres.search.SearchVectorField(
                        editable=False, null=True
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.Department",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universities.University",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="professor",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=[b"search_index"], name="professors__search__8d84b9_gin"
            ),
        ),
    ]
