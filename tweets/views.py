from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweet/create'
    login_url = '/admin/'
    # fields = ['user', 'content']


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweet/"


class TweetListView(ListView):
    def get_queryset(self):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    # =====================# Function Base view #===============#
    # def tweet_detail_view(request, id=1):
    #     obj = Tweet.objects.get(id=id)
    #     context = {
    #         "object": obj
    #     }
    #     return render(request, 'tweets/detail_view.html', context)
    #
    #
    # def tweet_list_view(request):
    #     queryset = Tweet.objects.all()
    #     context = {
    #         "object_list": queryset
    #     }
    #     return render(request, 'tweets/list_view.html', context)

    # def tweet_create_view(request):
    #     form = TweetModelForm(request.POST or None)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.save()
    #     context = {
    #         "form": form
    #     }
    #     return render(request, 'tweet/create_view.html', context)
