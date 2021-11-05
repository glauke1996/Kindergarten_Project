from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from . import models as noti_model
from reviews import forms

# Create your views here.


class BoardView(ListView):
    model = noti_model.Posting
    paginate_by = 12
    paginate_orphans = 5
    ordering = "-created"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     posts = noti_model.Posting.objects.all()
    #     context["posts"] = posts
    #     return context


def post_detail(request, pk):
    try:
        post = noti_model.Posting.objects.get(pk=pk)
        form = forms.CreateReviewForm()
        return render(
            request, "notifications/detail.html", {"post": post, "form": form}
        )
    except noti_model.Posting.DoesNotExist:
        return Http404
