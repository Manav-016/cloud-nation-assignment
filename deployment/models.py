from django.db import models
from django.core.validators import MinValueValidator

class RegionConfig(models.Model):
    country_name = models.CharField(max_length = 255, null = False, blank = False)
    city_name = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"
        db_table = 'Region'
        unique_together = ('country_name', 'city_name')

    def __str__(self):
        return self.country_name + "_" + self.city_name
    
class SupportedFrameworks(models.Model):
    framework_name = models.CharField(max_length = 255, null = False, blank = False)
    framework_img = models.ImageField('framework/img')

    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"
        db_table = 'Framework'

    def __str__(self):
        return self.framework_name

class CloudProvider(models.Model): # Ignore this for now, as we are taking hard codedly aws as cloud provider
    provider_name = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name = "Cloud Provider"
        verbose_name_plural = "Cloud Providers"
        db_table = 'Cloud Provider'

    def __str__(self):
        return self.provider_name

class DeploymentCloudInfo(models.Model): # here we store the creds of different cloud providers, if any users have multiple accounts with same or different cloud providers.
    cloud_provider = models.ManyToOneRel(CloudProvider, on_delete = models.SET_NULL)
    # this info about creds and stuff will be added by the user itself after creating an account and before deploying an application

    class Meta:
        verbose_name = "Deployment Cloud Info"
        verbose_name_plural = "Deployment Cloud Info"
        db_table = 'Deployment Cloud Info'

    def __str__(self):
        return self.cloud_provider
    
# want add enum in this
class VMConfigForPlans(models.Model): # this model, we have to make it for all the cloud providers that we support, here is just an example for AWS for now.
    deployment_cloud = models.ManyToOneRel(DeploymentCloudInfo, on_delete = models.DO_NOTHING)
    server_plan = models.CharField(max_length = 255, null = False, blank = False)
    # here onwards the fields will be according to the cloud provider, means for AWS it has AMI id, different for GCP, Azure etc.
    image_name = models.CharField(max_length = 255, null = False, blank = False)
    image_id = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name = "VM Config For Plan"
        verbose_name_plural = "VM Config For Plans"
        db_table = 'VM Config For Plan'

    def __str__(self):
        return self.deployment_cloud + "_" + self.image_name + "_" + self.image_id
    
class DBTypes(models.Model):
    db_type = models.CharField(max_length = 255, null = False, blank = False, unique = True) # like mysql, postgresql, etc.

    class Meta:
        verbose_name = "DB Type"
        verbose_name_plural = "DB Types"
        db_table = 'DB Type'

    def __str__(self):
        return self.db_type

class DBConfigForPlans(models.Model): # this model, we have to make it for all the cloud providers that we support, here is just an example for AWS for now.
    db_type = models.ManyToOneRel(DBTypes, on_delete = models.DO_NOTHING, null = False, blank = False)
    # here onwards the fields will be according to the db type, and other things like host, port etc.
    host = models.CharField(max_length = 255, null = False, blank = False)
    port = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name = "DB Config For Plan"
        verbose_name_plural = "DB Config For Plans"
        db_table = 'DB Config For Plan'

    def __str__(self):
        return self.host + "_" + self.port + "_" + self.db_type.db_type
    
class AbstractPlan(models.Model):
    plan_type = models.CharField(max_length = 15, null = False, blank = False, unique = True)
    storage = models.IntegerField(validators = [MinValueValidator(0)])
    bandwidth = models.IntegerField(validators = [MinValueValidator(0)])
    memory = models.IntegerField(validators = [MinValueValidator(0)])
    cpu = models.IntegerField(validators = [MinValueValidator(0)])
    monthly_cost = models.FloatField(validators = [MinValueValidator(0)])
    price_per_hour = models.FloatField(validators = [MinValueValidator(0)])

    class Meta:
        abstract = True

class ServerPlans(AbstractPlan):
    cloud_provider = models.ForeignKey(CloudProvider, on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name = "Server Plan"
        verbose_name_plural = "Server Plans"
        db_table = 'Server Plan'

    def __str__(self):
        return "SERVER_" + self.plan_type

class DBPlans(AbstractPlan):

    class Meta:
        verbose_name = "DB Plan"
        verbose_name_plural = "DB Plans"
        db_table = 'DB Plan'

    def __str__(self):
        return "DB_" + self.plan_type

# class ServerPlans(models.Model):    
#     server_plan = models.CharField(max_length = 255, null = False, blank = False)

#     class Meta:
#         verbose_name = "Server Plan"
#         verbose_name_plural = "Server Plans"
#         db_table = 'Server Plan'

#     def __str__(self):
#         return self.server_plan
    
class EnvConfig(models.Model):
    env_name = models.CharField(max_length = 255, null = False, blank = False, unique = True)
    # env_variables = models(EnvironmentVariables, on_delete = models.CASCADE, null = False, blank = False)

    class Meta:
        verbose_name = "Environment Config"
        verbose_name_plural = "Environment Config"
        db_table = 'Environment Config'

    def __str__(self):
        return "Environment Config"
    
class EnvVars(models.Model):
    env_config = models.ManyToOneRel(EnvConfig, on_delete = models.DO_NOTHING, null = False, blank = False)
    env_var_name = models.CharField(max_length = 255, null = False, blank = False)
    env_var_value = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name = "Environment Variables"
        verbose_name_plural = "Environment Variables"
        db_table = 'Environment Variables'

    def __str__(self):
        return self.env_var_name

class DeploymentConfig(models.Model):
    app_name: models.CharField(max_length = 255, null = False, unique = True, blank = False)
    # vc_info: models.ForeignKey(VCConfig, on_delete = models.CASCADE, null = False, blank = False) # This field will be used if there will be support for any version control systems like GitHub, GitLab, BitBucket etc.
    org_name: models.CharField(max_length = 255, null = False, blank = False)
    repo_link: models.URLField(null = False, blank = False, unique = True)
    repo_name: models.CharField(max_length = 255, null = False, blank = False)
    branch_name: models.CharField(max_length = 255, null = False, blank = False, unique = True)
    region_name: models.ManyToOneRel(RegionConfig, on_delete = models.DO_NOTHING, null = False, blank = False)
    framework_name: models.ManyToOneRel(SupportedFrameworks, on_delete = models.DO_NOTHING, null = False, blank = False)
    server_plan: models.ManyToOneRel(ServerPlans, on_delete = models.DO_NOTHING, null = False, blank = False)
    db_type: models.ManyToOneRel(DBTypes, on_delete = models.DO_NOTHING, null = False, blank = False)
    db_plans: models.ManyToOneRel(DBPlans, on_delete = models.DO_NOTHING, null = False, blank = False)
    env_config: models.OneToOneField(EnvConfig, on_delete = models.CASCADE, null = False, blank = False)

    class Meta:
        verbose_name = "Deployed App"
        verbose_name_plural = "Deployed Apps"          
        db_table = 'Deployed App'

    def __str__(self):
        return self.app_name
    

