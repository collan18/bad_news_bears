from django.shortcuts import render
from .models import Wine
from json import dumps
from .forms import SearchForm

# import HTTPresponse 
from django.http import HttpResponse, HttpResponseRedirect



# create a new function called 'Home'. This function is going to
# the traffic from the home page of the app/website. The function
# takes a request argument which will return what we want the user to see
# when they are sent to this route. 
def Home(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('Report')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'Home.html', {'form': form})
# Put some text writeup here.
    # return HttpResponse('<h1></h1>')

# Create your views here.

def Report(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        category = form.cleaned_data['Category']
    else:
        category = "White"
    # category = form.Category   
    search = Wine.objects.filter(Category=category).values("Alcohol", "Category", "Rating")[:100]
    data = dumps(list(search))
    return render(request, 'Report.html', {"data":data})

def Suggestion(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        category = form.cleaned_data['Category']
    else:
        category = "White"
    # category = form.Category   
    search = Wine.objects.filter(Category=category)[:10]

    return render(request, 'Suggestion.html', {"wine_list": search})
# def marketing_report_page(request):
#    return render(request, 'marketing_report.html', {})

#  def index():
#     latest_question_list = Wine.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

