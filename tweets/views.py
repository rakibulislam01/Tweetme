from django.views.generic import DetailView, ListView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create'
    login_url = '/admin/'
    # fields = ['user', 'content']


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self, queryset=None):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    queryset = Tweet.objects.all()

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
