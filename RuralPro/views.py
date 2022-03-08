from django.shortcuts import render

# Create your views here.
from RuralPro import models;


def platform_list(request):
    platform_request = models.platform.objects.all()
    return render(request, "test.html", {"platform_queryset": platform_request})
