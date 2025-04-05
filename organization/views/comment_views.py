from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import Comment


class CommentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Comment
    template_name = "organization/comment_detail.html"
    context_object_name = "comment"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = "organization/comment_form.html"
    fields = ["author", "article", "content"]
    success_url = reverse_lazy("comment-list")


class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    template_name = "organization/comment_form.html"
    fields = ["author", "article", "content"]
    success_url = reverse_lazy("comment-list")


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = "organization/comment_confirm_delete.html"
    success_url = reverse_lazy("comment-list")
