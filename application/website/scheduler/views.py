from django.http import HttpResponse
from scrapper.models.folder import Folder
from scrapper.models.website import Website
from scrapper.models.user import Test

def scheduler(request, interval: str) -> HttpResponse:
    test_element, _ = Test.objects.get_or_create(name=interval)
    test_element.update(counter=test_element.counter+1)
    return HttpResponse("Counter updated")

def scheduler2(request, interval: str) -> HttpResponse:
    folders = Folder.objects.filter(is_ready=True)
    for folder in folders:
        websites = Website.objects.filter(folder_id=folder.id, is_ready=True)
        if websites:
            #data to be scrapped
            print(folder)
            print(websites)
    return HttpResponse("xd")