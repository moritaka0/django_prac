from django.contrib import admin
from .models import User
from .models import GoodJobMsg


# Register your models here.
admin.site.register(User)
admin.site.register(GoodJobMsg)