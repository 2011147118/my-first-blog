from Tools.scripts.highlight import default_latex_document
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})


