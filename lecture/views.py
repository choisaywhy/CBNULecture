from django.shortcuts import render, redirect
import openpyxl
from .models import Lecture, LectureComment, College, Department
from .forms import LectureCommentForm
from accounts.models import Profile
from django.contrib.auth.models import User

def evalScore(lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    comments = lecture.comment.all()
    count = comments.count()
    score = 0

    for comment in comments:
        score += comment.star
    
    return score/count

def main(request):
    lectures = Lecture.objects.all()

    return render(request, 'lecture/main.html', {
        'lectures' : lectures,
    })

def detail(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    form = LectureCommentForm()

    return render(request, 'lecture/detail.html', {
        'lecture' : lecture,
        'form' : form,
    })

def createCommentToLecture(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    form = LectureCommentForm()

    if request.method == "POST":
        form = LectureCommentForm(request.POST)
        comment, created = LectureComment.objects.get_or_create(lecture=lecture, author=request.user, defaults={
            'star': 0,
            'content': 'none',
        })
        if form.is_valid() and created:
            comment.star = form.cleaned_data['star']
            comment.content = form.cleaned_data['content']
            comment.save()

            lecture.score = evalScore(lecture.id)
            lecture.save()
    # add ajax
    return render(request, 'lecture/detail.html', {
    'lecture' : lecture,
    'form' : form,
    })

def updateComment(request, comment_id):
    comment_queryset = LectureComment.objects.filter(pk=comment_id)
    comment = comment_queryset[0]
    
    if request.user == comment.author:
        if request.method == "POST":
            form = LectureCommentForm(request.POST)
            if form.is_valid():
                comment.content = request.POST['content']
                comment.author = request.user
                comment.save()

                jsonData = serializers.serialize('json',comment_queryset,indent=2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
                return HttpResponse(jsonData, content_type='application/json')
            else:
                print(form.errors)
                return redirect('lecture:detail', comment.lecture.id)
    return render(request, 'lecture/detail.html', {
    'lecture' : lecture,
    'form' : form,
    })

def deleteComment(request, comment_id):
    comment = LectureComment.objets.get(pk=comment_id)
    lecture = comment.lecture

    # add ajax
    if request.user == comment.author:
        comment.delete()
        lecture.score = evalScore(lecture.id)
        lecture.save()
    return redirect('lecture:detail', lecture.id)

def getComment(request, comment_id):
    lecture = LectureComment.objects.filter(pk=comment_id)
    jsonData = serializers.serialize('json',lecture,indent=2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(jsonData, content_type='application/json')


def searchLectrue(request):

    category = request.GET.get('category','')
    data = request.GET.get('search_data','')

    if data == '' or category == '':
        lectures = Lecture.objects.all()
    else:
        if category == '강의명':
            lectures = Lecture.objects.filter(title__contains=data)
        else:
            lectures = Lecture.objects.filter(prof=data)
    
    return render(request, 'lecture/main.html', {
        'lectures' : lectures,
    })
