from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render

@require_GET
def hi(request):
    return HttpResponse('<html><body>Hi!</body></html>')
