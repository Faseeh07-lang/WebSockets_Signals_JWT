from django.urls import path
from .views import SignUpView,Protectedview,Create_post,live_count_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('protectedView/',Protectedview.as_view(),name='protected'),
    path('Create_post/',Create_post.as_view(),name="createpost"),
    path('live_count/', live_count_view, name='live_count'),
]