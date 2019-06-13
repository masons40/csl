from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Employee)
admin.site.register(WebsiteEmailAddress)
admin.site.register(WebsitePhoneNumber)
admin.site.register(NewsArticle)

admin.site.register(NumberofSchoolsInConnacht)
admin.site.register(NumberofSchoolsInMunster)
admin.site.register(NumberofSchoolsInLeinster)
admin.site.register(NumberofSchoolsInUlster)

admin.site.register(jobPost)