from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from .models import Advertisement, Rubric


# Create your views here.






class MyOwnListView(ListView):
    model = Advertisement
    context_object_name = 'adv'
    template_name = 'advertisement.html'


def by_rubric(request, id):
    adv = Advertisement.objects.filter(rubric=id)

    rubric = Rubric.objects.get(pk=id)
    context = {'adv': adv , 'rubric':rubric}
    return render(request, 'by_rubric.html', context=context)




def rubric(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'rubrics.html', context=context)

