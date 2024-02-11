from django.shortcuts import render

# Create your views here.
def add_show(request):
    return render(request, 'crud_app/addandshow.html')