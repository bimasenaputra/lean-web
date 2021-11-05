"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
import dashboard.urls as dashboard
import login.urls as login
import grade_viewer.urls as grade
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
<<<<<<< HEAD
    path('login/', include('login.urls')),
    path('task-manager/', include('TaskManager.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('task-viewer/', include('task_viewer.urls'))
=======
    path('dashboard/', include(dashboard)),
    path('login/', include(login)),
    path('grade/', include(grade))

>>>>>>> 895d920d906c78739bbed892074bd829788cf032
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
