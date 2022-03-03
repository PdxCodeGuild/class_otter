from django.shortcuts import render
from rest_framework.views import APIView
from models import User

class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')
   
    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email, nickname=nickname, name=name, password= )
        


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        #login
        pass
