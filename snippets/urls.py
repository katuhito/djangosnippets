from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/new/', views.snippet_new, name="snippet_new"),
    path('snippets/<int:snippet_id>/', views.snippet_detail, name="snippet_detail"),
    path('snippets/<int:snippet_id>/edit/', views.snippet_edit, name="snippet_edit"),
]
