from django.shortcuts import render
from .forms import PostForm


def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        print("Success")
        form.save()
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'post_create.html', context)