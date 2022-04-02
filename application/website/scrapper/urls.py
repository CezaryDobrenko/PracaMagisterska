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
from scheduler.views import scheduler, scheduler2
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
    FolderCreate,
    FolderUpdate,
)
from scrapper.views.website.website_views import (
    WebsitesList,
    WebsitesDelete,
    WebsiteCreate,
    WebsiteUpdate,
    WebsitesClear
)
from scrapper.views.selector.selectors_views import (
    SelectorsList,
    SelectorsDelete,
    SelectorsCreate,
    SelectorsClear,
    SelectorsUpdate,
    SelectorsApprove,
    SelectorsCreateGUI
)
from scrapper.views.collected_data.data_views import (
    CollectedDataList,
    CollectedDataDelete,
    CollectedDataClear,
    CollectedDataUpdate
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
    path("folders/add/", FolderCreate.as_view(), name="folders-add"),
    path("folders/update/<int:pk>/", FolderUpdate.as_view(), name="folders-update"),
    path("folders/delete/<int:pk>/", FoldersDelete.as_view(), name="folders-delete"),

    path("websites/<int:pk>/", WebsitesList.as_view(), name="websites-settings"),
    path("websites/add/<int:pk>/", WebsiteCreate.as_view(), name="websites-add"),
    path("websites/update/<int:pk>/", WebsiteUpdate.as_view(), name="websites-update"),
    path("websites/delete/<int:pk>/", WebsitesDelete.as_view(), name="websites-delete"),
    path("websites/clear/<int:pk>/", WebsitesClear.as_view(), name="websites-clear"),

    path("selectors/<int:pk>/", SelectorsList.as_view(), name="selectors-list",),
    path("selectors/add/<int:pk>/", SelectorsCreate.as_view(), name="selectors-add",),
    path("selectors/add_gui/<int:pk>/", SelectorsCreateGUI.as_view(), name="selectors-add-gui"),
    path("selectors/delete/<int:pk>/", SelectorsDelete.as_view(), name="selectors-delete"),
    path("selectors/clear/<int:pk>/", SelectorsClear.as_view(), name="selectors-clear"),
    path("selectors/update/<int:pk>/", SelectorsUpdate.as_view(), name="selectors-update"),
    path("selectors/approve/<int:pk>/", SelectorsApprove.as_view(), name="selectors_approve"),

    path("collected_data/<int:pk>/", CollectedDataList.as_view(), name="collected-data-list",),
    path("collected_data/delete/<int:pk>/", CollectedDataDelete.as_view(), name="collected-data-delete"),
    path("collected_data/update/<int:pk>/", CollectedDataUpdate.as_view(), name="collected-data-update"),
    path("collected_data/clear/<int:pk>/", CollectedDataClear.as_view(), name="collected-data-clear"),

    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    path("scheduler/<interval>", scheduler, name="scheduler"),
    path("scheduler2/<interval>", scheduler2, name="scheduler2"),
]