from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import BookForm
from webapp.models import Book


def index_view(request, *args, **kwargs):
    books = Book.objects.all().filter(status='active').order_by('-created_at')

    return render(request, 'index.html', context={
        'books': books
    })

def add_new_note(request, *args, **kwargs):

    if request.method == 'GET':

        form = BookForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':

        form = BookForm(data=request.POST)

        if form.is_valid():

            Book.objects.create(

                name=form.cleaned_data['name'],

                email=form.cleaned_data['email'],

                text=form.cleaned_data['text'],

            )

            return redirect('index')

        else:

            return render(request, 'create.html', context={'form': form})

def note_update_view(request, pk):

        book = get_object_or_404(Book, pk=pk)

        if request.method == 'GET':

            form = BookForm(data={

                'name': book.name,

                'email': book.email,

                'text': book.text,

            })

            return render(request, 'update.html', context={'form': form, 'book': book})

        elif request.method == 'POST':

            form = BookForm(data=request.POST)

            if form.is_valid():

                book.name = form.cleaned_data['name']

                book.email = form.cleaned_data['email']

                book.text = form.cleaned_data['text']


                book.save()

                return redirect('index')

            else:

                return render(request, 'update.html', context={'form': form, 'book': book})


def note_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
        return redirect('index')



# Create your views here.
