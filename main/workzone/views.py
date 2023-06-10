from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        template = "workzone/main.html"
        return render(request, template)
    

class StorageView(View):
    def get(self, request):
        template = "workzone/storage.html"
        return render(request, template)
    

class ProfileView(View):
    def get(self, request):
        template = "workzone/myorders.html"
        return render(request, template)