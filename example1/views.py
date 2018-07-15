from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    response = HttpResponse(content_type='text/html')
    print(response.status_code)
    response.content = '<p>Nhung</p>'
    response.status_code = 404
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path")
