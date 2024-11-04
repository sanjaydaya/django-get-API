from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse

def ok(request):
    return render(request, 'ok.html')

def home(request):
    try:
        response = requests.get('https://www.atibadulla.edu.lk/')
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No Title Found'
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        response_data = {
            'title': title,
            'paragraphs': paragraphs,
        }
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=400)

