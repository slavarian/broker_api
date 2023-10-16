from django.shortcuts import render ,redirect
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from django.views import View
from .serializers import MyUserSerializers
from .models import MyUser
from .forms.login import LoginForm
from .forms.register import RegisterForm
from .forms.profile import UserProfileForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import (
    IsAuthenticated 
)

class UserViewSet(viewsets.ViewSet):
    queryset = MyUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(
            self ,
            request,
            *args,
            **kwargs,
    ) -> Response:
        serializer = MyUserSerializers(
            instance=self.queryset , many=True
        )
        return Response(
            data=serializer.data
        )

    def retrieve(
                self ,
                request:Request,
                pk:int = None
        ) -> Response:
        user = self.queryset.get(pk=pk)
        serialiser = MyUserSerializers(
                instance=user
            )
        return Response(
                data=serialiser.data
            )
   
    def post(self, request):
        serializer = MyUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response({'post': serializer.data})

class RegisterView(View):
    """
    User login.
    """

    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
                }
            )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            MyUser.objects.create(**form.cleaned_data)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
                }
            )

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile') 
            else:
                form.add_error(None, 'неверные данные')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', 
                  {'form': form}
                  )


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form , 'user': user})