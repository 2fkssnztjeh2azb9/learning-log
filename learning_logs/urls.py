"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

handler404 = views.handler404
handler500 = views.handler500

app_name = "learning_logs"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # Detailed page for a single topic
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
