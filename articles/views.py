from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'articles/home.html')

def article_20_raisons(request):
    return render(request, 'articles/20-raisons.html')

def article_bienfaits_sport(request):
    return render(request, 'articles/bienfaits-sport.html')

def article_conseils_debutant(request):
    return render(request, 'articles/conseils-debutant.html')

def article_rester_motive(request):
    return render(request, 'articles/rester-motive.html')

def article_bruler_calories(request):
    return render(request, 'articles/bruler-calories.html')

def article_etirements(request):
    return render(request, 'articles/etirements.html')

def search(request):
    try:
        query = request.GET.get('q', '').strip().lower()  # Assure que `query` est une chaîne valide
        all_articles = [
            {"title": "20 raisons de se mettre au sport", "url": "/articles/20-raisons/"},
            {"title": "15 bienfaits du sport sur la santé", "url": "/articles/bienfaits-sport/"},
            {"title": "10 conseils pour les débutants", "url": "/articles/conseils-debutant/"},
            {"title": "Comment rester motivé pour faire du sport", "url": "/articles/rester-motive/"},
            {"title": "Les meilleures activités pour brûler des calories", "url": "/articles/activites-calories/"},
            {"title": "L'importance des étirements après l'exercice", "url": "/articles/etirements-exercice/"},
        ]

        # Filtrer les articles contenant le mot-clé recherché
        results = [article for article in all_articles if query in article["title"].lower()]

        return render(request, 'articles/search_results.html', {'query': query, 'results': results})
    except Exception as e:
        return render(request, 'articles/search_results.html', {'query': None, 'results': [], 'error': str(e)})



# Create your views here.
