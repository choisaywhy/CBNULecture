from django.shortcuts import render, redirect

from .models import Lecture, LectureComment, College, Department
from .forms import LectureCommentForm
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.

def list(request):

    user = request.user
    return render(request, 'lecture/list.html', {
    })

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
        if form.is_valid():
            comment = LectureComment()
            comment.lecture = lecture
            comment.star = form.cleaned_data['star']
            comment.content = form.cleaned_data['content']
            comment.author = request.user
            comment.save()
    # add ajax
    return render(request, 'lecture/detail.html', {
    'lecture' : lecture,
    'form' : form,
    })

def updateComment(request, comment_id):
    comment = LectureComment.objets.get(pk=comment_id)

    if request.user == comment.author:
        if request.method == "POST":
            form = LectureCommentForm(request.POST)
            if form.is_valid():
                comment.star = form.cleaned_data['star']
                comment.content = form.cleand_data['content']
                comment.save()
    # add ajax
    return render(request, 'lecture/detail.html', {
    'lecture' : lecture,
    'form' : form,
    })

def deleteComment(request, comment_id):
    comment = LectureComment.objets.get(pk=comment_id)
    lecture = comment.lecture

    if request.user == comment.author:
        comment.delete()
        return redirect('lecture:detail', lecture.id)