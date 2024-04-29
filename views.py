from django.shortcuts import render
from .models import VisitLog

def index(request):
    # Логируем посещение страницы
    VisitLog.objects.create(page_visited="Главная")
    
    # Данные о вашем первом Django-сайте и о вас
    about_me_html = """
    <h2>О моем первом Django-сайте:</h2>
    <p>Добро пожаловать на мой первый Django-сайт!</p>
    """
    return render(request, 'index.html', {'content': about_me_html})

def about(request):
    # Логируем посещение страницы
    VisitLog.objects.create(page_visited="О себе")
    
    # Данные о вас
    about_me_html = """
    <h2>Обо мне:</h2>
    <p>Я создал этот сайт, чтобы научиться работать с Django.</p>
    """
    return render(request, 'about.html', {'content': about_me_html})
