from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(RegionConfig)
admin.site.register(SupportedFrameworks)
admin.site.register(CloudProvider)
admin.site.register(DeploymentCloudInfo)
admin.site.register(VMConfigForPlans)
admin.site.register(DBTypes)
admin.site.register(DBConfigForPlans)
admin.site.register(AbstractPlan)
admin.site.register(ServerPlans)
admin.site.register(DBPlans)
admin.site.register(EnvConfig)
admin.site.register(EnvVars)
admin.site.register(DeploymentConfig)
