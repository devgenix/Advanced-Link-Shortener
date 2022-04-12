from django.http.response import Http404
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import get_object_or_404

def home(request):

    return render(request, 'index.html')