from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):
    # 获取文章是为了把文章和评论关联起来
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，这是一个类字典对象
        form = CommentForm(request.POST)
        if form.is_valid:
            # 利用表单数据生成Comment模型类的实例
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # 当redirect接受一个模型实例时，会调用这个实例的get_absolute_url方法
            return redirect(post)
        else:
            # Comment和Post外键关联
            # 实例comment获取post：comment.post(.title | .author···)
            # 实例post获取comment：post.comment_set.all() = Comment.objects.filter(post=post)
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)