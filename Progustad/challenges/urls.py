from django.urls import path
from . import views
urlpatterns = [
    path('s/',views.challenges),
    path('/<int:id>',views.challengeDetail),
]