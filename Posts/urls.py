from django.urls import path
from .views import ListPostView, RetrievePostView

urlpatterns = [
    path('', ListPostView.as_view(), name='posts'),
    path('<int:pk>/', RetrievePostView.as_view(), name='post-details'),
]