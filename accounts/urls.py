from django.urls import path

from . import views

urlpatterns = [

    path('user/', views.UserListCreateAPiView.as_view(), name="user-list-create"),
    path('user/<int:pk>/', views.UserDetailApiView.as_view(), name="user-details"),
    path('user/delete/', views.DeleteUser.as_view(), name="user-delete"),
    path('user/activate/', views.ActivateUser.as_view(), name="user-activate"),
    path('user/deactivate/', views.DeActivateUser.as_view(), name="user-deactivate"),
    path('user/csv/', views.UserCsvDownLoad.as_view(), name="user-csv")

]