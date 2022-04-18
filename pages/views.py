from django.views.generic import ListView
from pages.models import Blog

class ListaBlogs(ListView):
    model = Blog
    template_name = 'pages/lista_blogs.html'

