from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from scrapper.models.folder import Folder
from django.views import View
from django.http import HttpResponse, JsonResponse
from scrapper.export import Export


class ExportList(LoginRequiredMixin, ListView):
    model = Folder
    template_name = "scrapper/export/export_list.html"
    paginate_by = 20
    ordering = ['pk']

    def get_queryset(self):
        folders = []
        for folder in Folder.objects.filter(user_id=self.request.user.id):
            folders.append(folder)
        return folders

class ExportJSON(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        export = Export(pk)
        data = export.export_as_json()
        response = JsonResponse(data, safe=False)
        response["Content-Disposition"] = f'attachment; filename="expoted_data.json"'
        return response


class ExportTXT(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        export = Export(pk)
        data = export.export_as_txt()
        response = HttpResponse(data)
        response["Content-Disposition"] = f'attachment; filename="expoted_data.txt"'
        return response

class ExportXML(LoginRequiredMixin, View):
    def get(self, request, pk):
        export = Export(pk)
        data = export.export_as_xml()
        response = HttpResponse(data)
        response["Content-Disposition"] = f'attachment; filename="expoted_data.xml"'
        return response

class ExportCSV(LoginRequiredMixin, View):
    def get(self, request, pk):
        export = Export(pk)
        data = export.export_as_csv()
        response = HttpResponse(data)
        response["Content-Disposition"] = f'attachment; filename="expoted_data.csv"'
        return response