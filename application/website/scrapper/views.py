from django.http import HttpResponse
from scrapper.models.user import Test

def test(request) -> HttpResponse:
    test_element, _ = Test.objects.get_or_create(name="test")
    current_counter_value = test_element.counter
    test_element.update(counter=current_counter_value+1)
    return HttpResponse(test_element.counter)