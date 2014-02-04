from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from website.models import Person, University

admin.site.register(Person)
admin.site.register(University)
