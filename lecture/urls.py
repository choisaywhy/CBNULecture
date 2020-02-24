from django.urls import path
from . import views

app_name='lecture'

urlpatterns = [
    path('', views.main, name='list'),
    path('detail/<int:lecture_id>', views.detail, name='detail'),
    path('addcomment/<int:lecture_id>', views.createCommentToLecture, name='addComment'),
    path('updatecomment/<int:comment_id>', views.updateComment, name='updateComment'),
    path('deletecomment/<int:comment_id>', views.deleteComment, name='deleteComment'),

]