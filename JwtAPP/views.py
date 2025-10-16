
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Post
from django.contrib.auth.password_validation import (
    validate_password,
    MinimumLengthValidator,
    UserAttributeSimilarityValidator,
)
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render


@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(View):
    def post(self,request):
        try:
            data=json.loads(request.body)
        except:
            return JsonResponse({"Message":"Failed to load Json data"})
        
        User=get_user_model()
        
        try:                                                       #This try is for email validation
            email_for_validation=data['email']
            validate_email(email_for_validation)
        except ValidationError as e:
            return JsonResponse({"Message":"Please Rewrite your email it is not valid", "Errror":str(e)})
        
        
        try:                                                       # And this try is for password validation
            password_for_validation=data['password']
            validate_password(
                password_for_validation,
                    password_validators=[
            MinimumLengthValidator(min_length=8),
            UserAttributeSimilarityValidator()
        ]
            )
        except ValidationError as e:
            return JsonResponse({"Message":"Please Rewrite your password is not valid", "Errror":str(e)})
            
            
        try:
          user=User.objects.create_user(
            email= email_for_validation,
            password= password_for_validation
          )
        except Exception as e:
            return JsonResponse({"Message": "Failed to create user", "error is": str(e)} )
        
        if user:
            return JsonResponse({"Message":"User has been created successfully"}, status=201)

class Protectedview(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return JsonResponse(
            {"message": f"The user is authenticated and its email is {user.email}"},
            status=200
        )
        
@method_decorator(csrf_exempt, name='dispatch')
class Create_post(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            title = request.POST.get('title')
            image = request.FILES.get('image')

            if not title or not image:
                return JsonResponse({"Message": "Title and image are required"}, status=400)

            new_post = Post.objects.create(
                title=title,
                image=image,
                user=request.user  
            )

            return JsonResponse({
                "Message": "The post has been saved successfully",
                "Post": new_post.title
            })

        except Exception as e:
            return JsonResponse({"Message": f"Fail to create the post: {str(e)}"}, status=500)
        
        
        
def live_count_view(request):
    count = Post.objects.count()
    return render(request, 'live_count.html', {'count': count})