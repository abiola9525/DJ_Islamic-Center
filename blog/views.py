from django.shortcuts import render, get_object_or_404
from . models import Post, Category
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from .forms import CommentForm
# Create your views here.

class postslist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blog.html'
    paginate_by = 6
    
class postdetail(FormMixin, generic.DetailView):
    model = Post
    template_name = 'blog-detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['category'] = self.object.category
        context['recent_posts'] = Post.objects.filter(status=1).order_by('-created_at')[:3]
        context['related_posts_count'] = Post.objects.filter(category=self.object.category).count()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(request.POST)
        print('request.POST')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user # Assuming user is logged in
            comment.post = self.object
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def get_success_url(self):
        return self.request.path

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.filter(status=1).order_by('-created_at')
    return render(request, 'category-post.html', {'category': category, 'posts': posts})