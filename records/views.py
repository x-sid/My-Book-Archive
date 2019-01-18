from django.shortcuts import render,get_object_or_404 
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Book
from .forms import BookForm
from django.contrib.auth.models import User
# Create your views here.
def book_list(request):
	books=Book.objects.filter(user=request.user)
	context={'books':books}
	return render(request,'records/book_list.html',context)

def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.user=request.user
            book.save()
            data['form_is_valid'] = True
            books = Book.objects.filter(user=request.user)
            data['html_book_list'] = render_to_string('records/partial_book_list.html', {'books': books})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def bookcreate(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'records/book_create.html')


def book_update(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'records/partial_book_update.html')

def book_delete(request,pk):
    book = get_object_or_404(Book,pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.filter(user=request.user)
        data['html_book_list'] = render_to_string('records/partial_book_list.html', {'books': books})
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('records/partial_book_delete.html',context,request=request,)
    return JsonResponse(data)









