"""
To render html web pages
"""
from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = 'Justin'
    number = random.randint(10, 1233123)
    article_obj = Article.objects.get(id=3)
    

    # from the database??
    # article-name
    # article_content

    context = {
        "title" : article_obj.title,
        "id" : article_obj.id,
        "content": article_obj.content
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", 
    context = context)
    
    # HTML_STRING = """
    # <h1>Hello {title} {id}</h1>
    # <p>Hello {content}<p>
    # """.format(**context)


    return HttpResponse(HTML_STRING)

