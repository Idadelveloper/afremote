from django.contrib import admin
from .models import (
    JobHunterProfile,
    Education,
    Experience,
    # Skills,
    # Interest
)

admin.site.register(JobHunterProfile)
admin.site.register(Education)
admin.site.register(Experience)
# admin.site.register(Skills)
# admin.site.register(Interest)
