from django.shortcuts import render
from rest_framework.views import APIView
 
class Sub(APIView):
    def get(self, request):
        print("Getttt")
        return render(request, "lab3/main.html")

    def post(self, request):
        print("Posttt")
        return render(request, "lab3/main.html")
