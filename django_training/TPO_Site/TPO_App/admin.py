from django.contrib import admin
from TPO_App.models import UserInfoModel, TrainingInfoModel,DocumentsModel, UserMarksModel

admin.site.register(UserInfoModel)
admin.site.register(TrainingInfoModel)
admin.site.register(DocumentsModel)
admin.site.register(UserMarksModel)
# Register your models here.
