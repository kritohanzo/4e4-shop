from django.urls import path, include
from core.decorators import worker_required, director_worker_required
from .views import IndexView, StorageView, ProfileView

app_name = 'workzone'

urlpatterns = [
    path('', worker_required(IndexView.as_view()), name='index'),
    path('profile/', worker_required(ProfileView.as_view()), name='profile'),
    path('storage/', worker_required(StorageView.as_view()), name='storage'),
    path('admin/', director_worker_required(IndexView.as_view()), name='admin'),
]