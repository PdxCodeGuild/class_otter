from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Discussion


class PostListView(generic.ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['message']

    def form_valid(self, form):
        discussion = Discussion.objects.create(user=self.request.user)
        post = Post.objects.create(discussion=discussion, author=self.request.user, message=form.cleaned_data['message'])
        return HttpResponseRedirect(reverse_lazy('posts:detail', args=[post.id]))

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['message']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author