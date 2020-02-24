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
    comment = LectureComment.objets.get(pk=comment_id)

    if request.user == comment.author:
        if request.method == "POST":
            form = LectureCommentForm(request.POST)
            if form.is_valid():
                comment.star = form.cleaned_data['star']
                comment.content = form.cleand_data['content']
                comment.save()

                lecture.score = evalScore(lecture.id)
                lecture.save()
    # add ajax
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