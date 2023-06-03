from django.shortcuts import redirect
from apps.blog.models import Post, Comment, Chef, About
from apps.blog.forms import CommentForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.


class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-upload_time']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recents = Post.objects.all().order_by('upload_time')[:6]
        comments = Comment.objects.filter(post=self.object)
        comments_count = Comment.objects.filter(post=self.object).count()
        comment_form = CommentForm()
        context['recents'] = recents
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['count'] = comments_count
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.object
            new_comment.save()

            return redirect(reverse('post_detail', kwargs={'pk': self.object.pk}))

        return self.render_to_response(self.get_context_data(comment_form=comment_form))





class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['chefs'] = Chef.objects.all()
        return context
