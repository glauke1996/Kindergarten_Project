from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib import messages
from . import forms
from notifications import models as noti_model

# Create your views here.


def create_comment(request, pk):
    if request.method == "POST":
        form = forms.CreateCommentForm(request.POST)
        try:
            post = noti_model.Posting.objects.get(pk=pk)
        except noti_model.Posting.DoesNotExist:
            return redirect(reverse("core:home"))
        if form.is_valid():
            comment = form.save()
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "답글이 등록되었습니다.")
            return redirect(reverse("notifications:detail", kwargs={"pk": post.pk}))
