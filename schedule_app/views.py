from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VisitorInfo
# from .serializers import VisitorInfoSerializer
from rest_framework import status
import base64
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash

def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('form')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['Password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('form')
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'login_form.html')


@login_required(login_url='/')
def visitor_form(request):
    if request.method == 'POST':
        return HttpResponse("Form Submitted")
    else:
        return render(request, 'registration.html')

class VisitorInfoAPI(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request):
        try:
            image_data = request.POST.get('user_image')
            format, imgstr = image_data.split(';base64,')
            file_name = '.'.join((str(request.POST.get('name')), 'png'))
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
                        
            VisitorInfo.objects.create(name=request.POST.get('name'), email=request.POST.get('email'),
                                       mobile_no=request.POST.get('number'),
                                       person_to_meet=request.POST.get('name_person'),
                                       address=request.POST.get('address'),
                                       from_time=request.POST.get('from_time'),
                                       to_time=request.POST.get('to_time'),
                                       visitor_image=data)
            return Response("Successfully Created", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)        

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        # form = PasswordChangeForm(request.user, request.POST)        
        old_password = request.POST['old_password']
        new_password = request.POST['new_password1']
        confirm_password = request.POST['new_password2']
        if not request.user.check_password(old_password):
        # if not request.user.is_authenticated():
            return render(request, 'change_password.html', context={'message': 'Incorrect Old Password. Try again'})
        if not new_password == confirm_password:
            return render(request, 'change_password.html', context={'message': 'New Password mismatch. Try again'})
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        return render(request, 'registration.html', context={'message': 'Password Changed Successfully'})
    return render(request, 'change_password.html')            


