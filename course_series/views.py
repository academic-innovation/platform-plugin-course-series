from django.http import HttpResponse


def test_page(request):
    """Returns a test response."""
    return HttpResponse("Hello, from platform-plugin-course-series!")
