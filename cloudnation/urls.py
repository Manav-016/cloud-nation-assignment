"""
URL configuration for cloudnation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deploy-app/', )
]

# UserInfo

# -  user data like name email etc.
# -  user GitHub email id for getting info about their GitHub account ( like organisations, repositories, branches etc.)



# AppInfo 
# -  app name
# -  region
# -  frame work
# -  env info
# -  server plan type -> f_key to the plans table
# -  DB plan type -> f_key to the db_plans table
# -  DB type -> f_key to the db_types table
# -  user GitHub email id for getting info about their GitHub account ( like organisations, repositories, branches etc.)




# Plans 
# -  plan type
# -  storage
# -  bandwidth
# -  memory ( ram )
# -  cpu
# -  monthly cost
# -  price per hour 


# ServerPlans(Plans)

# ==> here the question is, do we supposed to make the decision of which cloud service is to be selected for each plan according to our costing and our easiness to achieve win win for both user and us, or do we give user permission to choose those??


# DBPlans(Plans)

# ==> same question as server plans, and also that what is this Database type??



