from django.http import  HttpResponse


def home_page(request):
    print("Home page is requested")
    return HttpResponse("<h1>This is homepage</h1>")

def blank(request):
    print("First Page")
    return HttpResponse("<h1>Welcome to first Page</h1>")