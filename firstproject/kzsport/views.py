from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, "kzsport/index.html")

def city(request):
    return render(request, "kzsport/city.html")

def sport(request):
    sportsmen = {'sportsmen' : Sportsman.objects.all()}
    return render(request, "kzsport/sport.html", sportsmen)

def university(request):
    universities = {'universities' : University.objects.all()}
    return render(request, "kzsport/university.html", universities)

def food(request):
    return render(request, 'kzsport/food.html')

def show_tradition(request, tradition_slug):
    tradition = get_object_or_404(Tradition, slug = tradition_slug)
    context = {'tradition' : tradition}
    return render(request, 'kzsport/show_traditions.html', context = context)

def feedback(request):
    shelf = Feedback.objects.all()
    return render(request, 'kzsport/feedback.html', {'shelf': shelf})

def upload(request):
    upload = FeedbackCreate()
    if request.method == 'POST':
        upload = FeedbackCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('feedback')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'feedback'}}">reload</a>""")
    else:
        return render(request, 'kzsport/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Feedback.objects.get(id = book_id)
    except Feedback.DoesNotExist:
        return redirect('feedback')
    book_form = FeedbackCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('feedback')
    return render(request, 'kzsport/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Feedback.objects.get(id = book_id)
    except Feedback.DoesNotExist:
        return redirect('feedback')
    book_sel.delete()
    return redirect('feedback')

def signin(request):
    sign = UserCreate() 
    if request.method == "POST":
        sign = UserCreate(request.POST, request.FILES)
        if sign.is_valid():
            sign.save()
            send_mail("Web programming:back end", "My content",
              "200103092@stu.sdu.edu.kz",
               [request.POST.get('email')],
               fail_silently=False, html_message="<b>Bold text</b><i> Italic text</i>"
                )
            return redirect('home')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "">reload</a>""")
    else:
        return render(request, 'kzsport/login.html', {'sign_form':sign})


def send_message(request):
    send_mail("Web programming:back end", "My content",
               "200103092@stu.sdu.edu.kz",
               ["200103092@stu.sdu.edu.kz", "galikhandias@gmail.com"],
               fail_silently=False, html_message="<b>Bold text</b><i> Italic text</i>"
               )
    return render(request, 'kzsport/email.html')