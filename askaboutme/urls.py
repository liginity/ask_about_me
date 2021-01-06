from django.urls import path

from askaboutme import views

app_name = "askaboutme"
urlpatterns = [
    path("", views.index, name="index"),
    path("ask-a-question/", views.ask_a_question, name="askq"),
]
