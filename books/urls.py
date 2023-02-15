from Token.jwtToken import MyTokenObtainPairView
from django.conf.urls import url
from books import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view-items'),
    path('update/', views.update_items, name='update-items'),
    path('ebook/<int:pk>/delete/', views.delete_items, name='delete-items'),
    path('register/', views.register_user, name='registration'),
    # path('login/', views.login, name='User-login'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
# url(r'^ebook$',views.ebookApi),
# url(r'^ebook/([0-9]+)$',views.ebookApi),
# url(r'^ebook/(?P<title>.+)$',views.ebookList.as_view())
