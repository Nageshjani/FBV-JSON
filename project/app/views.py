
from .models import Book
from django.http import JsonResponse
import json
from django.http import JsonResponse
from .models import Book

def books(request):
    queries = Book.objects.all()
    book_list = list(queries.values())
    return JsonResponse({'books': book_list}, safe=False)





def book_detail(request, pk):
    try:
        book = Book.objects.filter(pk=pk).values()[0]
        #book = Book.objects.get(pk=pk)
        if book is None:
            return JsonResponse({'error': 'Book does not exist'}, status=404)
        return JsonResponse({'book': book}, safe=False)
    
    except :
        return JsonResponse({'error': 'Invalid value for primary key'}, status=400)




def book_create(request):
    print(request.content_type)
    if request.method == 'POST':
        if request.content_type == 'application/x-www-form-urlencoded':
            try:
                title = request.POST.get('title')
                author = request.POST.get('author')
            except:
                return JsonResponse({'message':'Error While fetching the data'})

        elif request.content_type == 'multipart/form-data':
            try:
                title = request.POST.get('title')
                author = request.POST.get('author')
            except:
                return JsonResponse({'message':'Error While fetching the data'})


        elif request.content_type == 'text/plain':
            try:

                json_string = request.body.decode('utf-8')
                data = json.loads(json_string)
                title = data.get('title')
                author = data.get('author')
            except:
                return JsonResponse({'message':'Error While fetching the data'})

        elif request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
                title = data.get('title')
                author = data.get('author')
            except:
                return JsonResponse({'message':'Error While fetching the data'})
        else:
            return JsonResponse({'message': 'Unsupported media type!'}, status=415)

        book = Book.objects.create(title=title, author=author)
        book.save()

        return JsonResponse({'message': 'Successfully created','book': {
                'id': book.id,
                'title': book.title,
                'author': book.author,
        }})

    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=400)










def book_update(request, pk):
    print(request.content_type)
    if request.method == 'POST':
        try:
            book=Book.objects.get(pk=pk)
            if book is None:
                    return JsonResponse({'error': 'Book does not exist'}, status=404)

            if request.content_type == 'application/x-www-form-urlencoded':
                try:
                    book.title = request.POST.get('title')
                    book.author = request.POST.get('author')
                except:
                    return JsonResponse({'message':'Error While fetching the data'})

            elif request.content_type == 'multipart/form-data':
                try:
                    book.title = request.POST.get('title')
                    book.author = request.POST.get('author')
                except:
                    return JsonResponse({'message':'Error While fetching the data'})


            elif request.content_type == 'text/plain':
                try:

                    json_string = request.body.decode('utf-8')
                    data = json.loads(json_string)
                    book.title = data.get('title')
                    book.author = data.get('author')
                except:
                    return JsonResponse({'message':'Error While fetching the data'})

            elif request.content_type == 'application/json':
                try:
                    data = json.loads(request.body.decode('utf-8'))
                    book.title = data.get('title')
                    book.author = data.get('author')
                except:
                    return JsonResponse({'message':'Error While fetching the data'})
            else:
                return JsonResponse({'message': 'Unsupported media type!'}, status=415)

            book.save()

            return JsonResponse({'message': 'Successfully created','book': {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
            }})
        except:
            return JsonResponse({'error': 'Invalid value for primary key'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=400)





    
    

def book_delete(request, pk):
    try:
        #book = get_object_or_404(Book, pk=pk)
        book=Book.objects.get(pk=pk)
        print('-------------',book)
        if request.method == 'DELETE':
            book.delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Only DELETE requests are allowed.'})
    except:
        return JsonResponse({'status': 'error', 'message': 'Either item is not included in database or something else is wrong.'})


