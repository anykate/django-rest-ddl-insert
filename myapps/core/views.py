from django.shortcuts import render, redirect
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Color
from .serializers import ColorSerializer
from .forms import ColorInsertForm
import requests


# Create your views here.
@api_view(['POST'])
def savecolor_api(request):
    if request.method == 'POST':
        serialized_color_obj = ColorSerializer(data=request.data)
        if serialized_color_obj.is_valid():
            serialized_color_obj.save()
            return Response(serialized_color_obj.data, status=status.HTTP_201_CREATED)
        return Response(serialized_color_obj.data, status=status.HTTP_400_BAD_REQUEST)


def savecolor(request):
    form = ColorInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            post_data = requests.post(
                'http://localhost:8000/api/colornew/',
                headers={'Content-Type': 'application/json'},
                json=form.cleaned_data
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
