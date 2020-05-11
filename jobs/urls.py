from django.urls import path

from .views import home_page

"""  Namespace usage:

<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></
˓→li>
"""
app_name = "jobs"
urlpatterns = [
    path("", home_page, name="home"),
]
