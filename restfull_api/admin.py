from django.contrib import admin


#email=zafaraftab@gmail.com
#username=aftab
#password=same for everywhere

# Register your models here.

from . import models
admin.site.register(models.UserProfile)