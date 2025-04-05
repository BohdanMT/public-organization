from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import Article


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = "organization/article_detail.html"
    context_object_name = "article"

class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    template_name = "organization/article_form.html"
    fields = ["title", "content", "author"]
    success_url = reverse_lazy("article-list")

class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    template_name = "organization/article_form.html"
    fields = ["title", "content", "author"]
    success_url = reverse_lazy("article-list")

class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    template_name = "organization/article_confirm_delete.html"
    success_url = reverse_lazy("article-list")
