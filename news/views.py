from django.shortcuts import render,redirect
from .models import articls
from .forms import articlsform
from django.urls import reverse
from django.views.generic import DetailView

def news_home(request):
    news=articls.objects.all()
    return render(request,'news/news_home.html',{'news':news})

class NewsDetailView(DetailView):
    model=articls
    template_name='news/details_view.html'
    context_object_name='article'
    pk_url_kwarg = 'pk'
 

def create(request):
    error = ''
    if request.method == "POST":
        form = articlsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Saved successfully!")
            return redirect('news_home')
        else:
            print("Form is not valid:", form.errors)
    
    form = articlsform()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)