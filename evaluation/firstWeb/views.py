from django.shortcuts import render
from django.http import HttpResponse
from statistics import mean

from .models import basicInfo, commentInfo

def Index(request):
    # return render(request, 'index.html')
    return HttpResponse('HELLO WORLD FOR YOU')

def Overview(request):
    pass

def ShowBasicdata(request):
    basic_info = basicInfo.objects.all
    return render(request, 'shows.html', context={'basic_info': basic_info})

def Detail(request, question_id):
    basic_info = basicInfo.objects.all
    comment_info = commentInfo.objects.all
    return render(request, 'detail.html', context={'basic_info': basic_info, 'comment_info': comment_info})

    # return HttpResponse("Now it's the %d info" % question_id)

def Cal(request):
    plot = float(request.POST['plot'])
    actor_expression = float(request.POST['actor_expression'])
    direction = float(request.POST['direction'])
    screenwriter = float(request.POST['screenwriter'])
    photography = float(request.POST['photography'])
    music = float(request.POST['music'])
    art = float(request.POST['art'])
    effects = float(request.POST['effects'])
    overall = str(request.POST['overall'])

    rating = mean([plot, actor_expression, direction, screenwriter, photography, music, art, effects])

    current_user = 1
    basicinfo_id = 1

    commentInfo.objects.create(plot=plot, actor_expression=actor_expression, direction=direction,
                               screenwriter=screenwriter, photography=photography, music=music,
                               art=art, effects=effects, overall=overall, rating=rating,
                               user_id=current_user, basicinfo_id=basicinfo_id)
    return render(request, 'cal.html', context={'rating': rating})


