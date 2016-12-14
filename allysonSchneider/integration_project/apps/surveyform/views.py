from django.shortcuts import render, HttpResponse, redirect

# Create your views here.



def index(request):

    if 'name' in request.session:
        request.session['submission'] += 1
        del request.session['name']
        del request.session['location']
        del request.session['language']
        del request.session['comment']
    return render(request, 'surveyform/index.html')

def process(request):
    request.session['name'] = request.POST['Name']
    request.session['location'] = request.POST['Location']
    request.session['language'] = request.POST['Language']
    request.session['comment'] = request.POST['Comment']
    return redirect('survey:result')

def result(request):
    print request.POST
    survey = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'submission': request.session['submission'],
    }
    return render(request, 'surveyform/result.html', survey)
