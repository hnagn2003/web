from django.contrib import admin
from mainapp.models import UserRating, SaveForLater, AllBooks

# Register your models here.

admin.site.register(UserRating)
admin.site.register(SaveForLater)
admin.site.register(AllBooks)