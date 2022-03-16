from django.http import HttpResponse
from scrapper.models.user import Test

def scheduler(request, interval: str) -> HttpResponse:
    test_element, _ = Test.objects.get_or_create(name=interval)
    test_element.update(counter=test_element.counter+1)
    return HttpResponse("Counter updated")