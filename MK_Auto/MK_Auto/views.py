from django.shortcuts import render


def view_index(request):
    context = {}
    return render(request, "index.html", context)
