from typing import Any

import time
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from app.models import Article, Internship
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def index(request):
    namespace = request.resolver_match.namespace
    context = {}

    if namespace == "articles":
        context["title"] = "Articles"
        # maybe filter for articles
    elif namespace == "internships":
        context["title"] = "Internships"
        context["internships"] = Internship.objects.all()
        # maybe filter for internships

    return render(request, "app/index.html", context)


# This view displays a list of articles.
# Only logged-in users can access this view, enforced by LoginRequiredMixin.
# It filters the queryset to show only the articles created by the currently logged-in user.
class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"
    paginate_by = 5


    # This method customizes the queryset to show only articles
    # created by the logged-in user, ordered by creation time (newest first)
    def get_queryset(self) -> QuerySet[Any]:
        search=self.request.GET.get("search")
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset.order_by("-created_at")

# -------------------------------
# ArticleCreateView
# -------------------------------
# This view handles article creation.
# Only logged-in users can create articles (LoginRequiredMixin).
class ArticleCreateView(LoginRequiredMixin,CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title","status","content","twitter_post"]
    success_url = reverse_lazy("articles:home")

     # This method sets the creator of the article to the currently logged-in user
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
# -------------------------------
# ArticleUpdateView
# -------------------------------
# This view handles updating articles.
# Only logged-in users can access it (LoginRequiredMixin).
# UserPassesTestMixin ensures only the creator of the article can update it.
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title","status","content","twitter_post"]
    success_url = reverse_lazy("articles:home")
    context_object_name = "articles"

    #verfies that logged in user, is the creator of the object
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator

# -------------------------------
# ArticleDeleteView
# -------------------------------
# This view handles deleting articles.
# Only the logged-in user who created the article can delete it.
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("articles:home")
    context_object_name = "articles"

     # Only allow deletion if the user is the creator of the article
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator
    
    def post(self, request: HttpRequest,*args:str, **kwargs:Any)-> HttpResponse:
        messages.success(request,"Article deleted successfully.", extra_tags="error")
        return super().post(request,*args,**kwargs)
    

# List view to display all internships
class InternshipListView(ListView):
    template_name = "app/internship.html"
    model = Internship
    context_object_name = "internships"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        search=self.request.GET.get("search")
        queryset = super().get_queryset()
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset.order_by("-created_at")

# View to create a new internship (requires login)
class InternshipCreateView(LoginRequiredMixin,CreateView):
    template_name = "app/internship_create.html"
    model = Internship
    fields = ["title","content","company","location","url_link","status"]
    success_url = reverse_lazy("internships:internship")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

# View to update an existing internship (requires login and creator permission)
class InternshipUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "app/internship_update.html"
    model = Internship
    fields = ["title","content","company","location","url_link","status"]
    success_url = reverse_lazy("internships:internship")
    context_object_name = "internship"

    #verfies that logged in user, is the creator of the object
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator

# View to delete an internship (requires login and creator permission)
class InternshipDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name = "app/internship_delete.html"
    model = Internship
    success_url = reverse_lazy("internships:internship")
    context_object_name = "internship"

    #verfies that logged in user, is the creator of the object
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creator
    
    # Handle POST requests for deleting the internship
    def post(self, request: HttpRequest,*args:str, **kwargs:Any)-> HttpResponse:
        
        # Add a success message to notify the user of successful deletion
        messages.success(request,"Internship deleted successfully.", extra_tags="error")
        
        # Call the parent class's post method to perform the deletion
        return super().post(request,*args,**kwargs)
    

    






