"""scrapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from scheduler.views import scheduler
from scrapper.views.basic_views import (
    DashboardView,
    AboutView,
    MissionView,
    AuthorView,
    ContactView,
    ProcessView,
    RegisterView
)
from scrapper.views.login import (
    LoginView,
    StatisticView,
    PrivateDashboardView
)

from scrapper.views.folder.folder_views import (
    FoldersList,
    FoldersDelete,
)


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("dashboard/", PrivateDashboardView.as_view(), name="private_dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("about/", AboutView.as_view(), name="about"),
    path("mission/", MissionView.as_view(), name="mission"),
    path("author/", AuthorView.as_view(), name="author"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("process/", ProcessView.as_view(), name="process"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("statistics/", StatisticView.as_view(), name="statistics"),
    path("folders/", FoldersList.as_view(), name="folders"),
    path("folders/delete/<int:pk>/", FoldersDelete.as_view(), name="folders-delete",),
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    path("scheduler/<interval>", scheduler, name="scheduler"),
]