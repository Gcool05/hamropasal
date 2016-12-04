from django.shortcuts import render

# Create your views here.
def get_categories(request):
    return {
        'body': 'hello categories',
    }