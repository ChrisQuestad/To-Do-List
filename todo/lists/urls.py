from django.urls import path
from .views import *

app_name = 'lists'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create', ListCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ListDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ListUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ListDeleteView.as_view(), name='delete'),
    path('<int:list_pk>/task/create', TaskCreateView.as_view(), name='task-create'),
    path('<int:list_pk>/task/update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('<int:list_pk>/task/delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),

]
