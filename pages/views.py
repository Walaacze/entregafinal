from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from pages.models import Blog

class ListaBlogs(ListView):
    model = Blog
    template_name = 'pages/lista_blogs.html'
    
class DetalleBlogs(DetailView):
    model = Blog
    template_name = 'pages/detalle_blogs.html'
    
class CrearBlog(CreateView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
    
class BorrarBlog(DeleteView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
    
class ActualizarBlog(UpdateView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha']
