from django.contrib import admin
from .models import Tags_Question
from .models import Profile
from .models import Question
from .models import Answer

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tags_Question)

# Register your models here.
