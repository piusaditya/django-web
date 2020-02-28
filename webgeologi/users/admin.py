from django.contrib import admin
from .models import Profile


# Register models dengan import models users ke admin juga
admin.site.register(Profile)