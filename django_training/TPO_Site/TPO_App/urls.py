from django.conf.urls import include
from django.urls import path
from TPO_App import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'TPO_App'

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('login/',views.UserLoginView, name='user_login'),
    path('registration/', views.UserRegistrationView, name="user_registration"),
    path('placement/',views.PlacementView,name="placement"),
    path('logout/', views.UserLogoutView, name='user_logout'),
    #path('<str:username>/', views.UserInfoView, name="profile"),
    path('<str:username>/editinfo/', views.UserEditInfoView, name="edit_info"),
    path('<str:username>/marksdetails/', views.UserMarksView, name="marks_details"),
    path('<str:username>/trainingdetails/', views.TrainingDetailsView, name="training_details"),
    path('<str:username>/documentsdetail/', views.DocumentsView, name="documents_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)