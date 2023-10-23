
from django.urls import path
from .views import MyOwnListView,by_rubric, rubric



app_name = 'advertisement'

urlpatterns = [


    path('adv/', MyOwnListView.as_view(), name='advertisement'),
    path('rubric/', rubric,),
    path('<int:id>/', by_rubric, name='rubrics'),

]
