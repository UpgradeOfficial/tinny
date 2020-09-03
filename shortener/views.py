from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.utils.crypto import get_random_string
from .serializers import URLShortenerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






from .models import URLShortener, Record
from .forms import URLShortenerForm, NewUserForm, urlify, unique_url_id

# Create your views here.

def home(request):
    url_form = URLShortenerForm()
    context={'u_form':url_form}
    if request.POST:
        
        url=URLShortenerForm(data=request.POST).save(commit=False)
        
        url.save()
        id= url.unique_id
        data = {'id':id}
        print(data)
        return JsonResponse(data)
            
    return render(request, 'shortener/index.html', context)
 
       
             
                         
def   url_redirect(request, unique_id):
    id = get_object_or_404(URLShortener, unique_id=unique_id)
    if id.active:
        url = id.url
    
        id.record_set.create()
        return redirect(url)
    raise Http404('URL Locked')
     
    context = {'u_form': url_form}
    return render(request, 'shortener/index.html', context)   
    
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context={"form":form}
    return render(request, "shortener/login.html", context)
    
    
def logout_view(request):
    logout(request)
    return  render(request, 'shortener/logout.html')
    
def register(request):
    form = NewUserForm()
    return render(request,
                     "shortener/register.html",
                    context={"form":form})
    
    
    
def dashboard(request):
    return render(request, 'shortener/dashboard.html')

def search_id(request):
    id=urlify(request.GET.get('id').lower())
    data = {'available': True}
    if URLShortener.objects.filter(unique_id=id).exists():
        data = {'available': False}
        return JsonResponse(data)
    
    return JsonResponse(data)
    
@api_view(['GET'])    
def search(request):
    filter = request.GET.get("filter")
    
    urls=URLShortener.objects.filter(Q(url__icontains=filter) | Q(unique_id__icontains=filter))
    
    
    
    page = request.GET.get('page', 1)
    paginator = Paginator(urls, 5)
    try:
        urls = paginator.page(page)
    except PageNotAnInteger:
        urls = paginator.page(1)
    except EmptyPage:
        urls = paginator.page(paginator.num_pages)
    serializer = URLShortenerSerializer(urls, many=True)
    print(serializer.data)
    return Response(serializer.data)
