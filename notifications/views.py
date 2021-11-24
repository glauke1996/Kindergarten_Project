from django.db.models import fields
from django.forms.forms import Form
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models as noti_model
from reviews import forms
from notifications import forms as noti_forms
from users import mixins

# Create your views here.


class BoardView(ListView):
    model = noti_model.Posting
    paginate_by = 14
    paginate_orphans = 5
    ordering = "-created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notifications = noti_model.Posting.objects.filter(notification=True)
        context["notifications"] = notifications
        return context


@login_required
def post_detail(request, pk):
    try:
        post = noti_model.Posting.objects.get(pk=pk)
        form = forms.CreateCommentForm()
        user_comment = None
        if request.method == "POST":
            print(request.POST)
            comment_form = forms.CreateCommentForm(request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.post = post
                user_comment.user = request.user
                user_comment.save()
                return HttpResponseRedirect(
                    reverse("notifications:detail", kwargs={"pk": pk}),
                    {"post": post, "form": form},
                )  ## to prevent us from double submit
        return render(
            request, "notifications/detail.html", {"post": post, "form": form}
        )
    except noti_model.Posting.DoesNotExist:
        return Http404


def search(request):
    filter_args = {}
    keyword = request.GET.get("keyword")
    print(keyword)
    if keyword != None:
        filter_args["title__contains"] = keyword
        results = noti_model.Posting.objects.filter(**filter_args)

    else:
        results = noti_model.Posting.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(results, 12, orphans=5)
    posts = paginator.page(int(page))
    return render(
        request,
        "notifications/search.html",
        {"page": posts, "keyword": keyword},
    )


class PostPhotosView(DetailView):
    model = noti_model.Posting
    template_name = "notifications/post_photos.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        if post.user.pk != self.request.user.pk:
            raise Http404()
        return post


class EditPhotoView(UpdateView):

    model = noti_model.Photo
    template_name = "notifications/photo_edit.html"
    fields = ("caption",)
    pk_url_kwarg = "photo_pk"

    def get_success_url(self):
        post_pk = self.kwargs.get("post_pk")
        return reverse("notifications:photos", kwargs={"pk": post_pk})


class AddPhotoView(FormView):
    template_name = "notifications/photo_create.html"
    form_class = noti_forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        return redirect(reverse("notifications:photos", kwargs={"pk": pk}))


class UploadPostView(mixins.LoggedInOnlyView, FormView):
    template_name = "notifications/post_create.html"
    form_class = noti_forms.CreatePostForm

    def form_valid(self, form):
        noti = self.request.POST.get("notificataion")
        if noti == "on":
            bool = True
        else:
            bool = False
        pk = self.request.user.pk
        form.save(pk, bool)
        return redirect("/notifications/")


@login_required
def delete_photo(request, post_pk, photo_pk):
    user = request.user
    try:
        post = noti_model.Posting.objects.get(pk=post_pk)
        if post.user != user:
            messages.error(request, "You are not athorized")
        else:
            noti_model.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("notifications:photos", kwargs={"pk": post_pk}))
    except noti_model.Posting.DoesNotExist:
        return redirect(reverse("core:home"))
