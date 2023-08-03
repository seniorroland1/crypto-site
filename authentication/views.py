from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from dashbaord.models import Profile
from dashbaord.helper import generate_referal_code
from django.db.models import F

class RegisterView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data['userName'] is None:
                response['message'] = 'Username is required'
                raise Exception('User field is None')
            
            if data['userEmail'] is None:
                response['message'] = 'Email is required'
                raise Exception('Email field is None')
            
            
            if data['userPassword'] is None:
                response['message'] = 'Password is required'
                raise Exception('Password field is None')
            
            
            if User.objects.filter(username = data['userName']).first() is not None:
                response['message'] = 'Username already taken '
                raise Exception('Username already taken')    
            
            if User.objects.filter(username = data['userEmail']).first() is not None:
                response['message'] = 'email already taken '
                raise Exception('email already taken')
            
            user = User.objects.create(username = data['userName'],email=data['userEmail'],password=data.get('userPassword'))  
            user.save()
            Profile.objects.create(user = user,nickname=data['userName'],referal = generate_referal_code(data['userName']))
            # Referals.objects.create(referal = generate_referal_code(data['userName']))
            
            try: 
                if data['referal']:
                    try:
                        referal_user = Profile.objects.filter(referal = data['referal']).first()
                    except:           
                        referal_user = None
                    
                    if referal_user:
                        Profile.objects.filter(referal=data['referal']).update(referal_point=F('referal_point') + 5)
                else:
                    pass
            except Exception as e:
                print(e)    
            response['status'] = 200
            response['message'] = 'User successfully registered'
            
        except Exception as e:
            print(e)
        
        return Response(response)
        
class LoginView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            
            if data['userName'] is None:
                response['message'] = 'Username is required'
                raise Exception('User field is None')
            
            if data['userPassword'] is None:
                response['message'] = 'Password is required'
                raise Exception('Password field is None')
            
            user = authenticate(request,username=data['userName'],password=data.get('userPassword'))
            if user:
                # login(request,user)
                response['status'] = 200    
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid Password'  
        except Exception as e:
            print(e)
            
        return Response(response)
    
def logout_page(request):
    logout(request)
    return redirect('/login')
    