from django.urls import path, include
from. import views


app_name = "orders"
urlpatterns = [
    path("", views.process_order, name="order"),
    
]
