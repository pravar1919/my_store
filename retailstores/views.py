from .models import Store
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def test(request):
    context = {'name': 'Pravar'}
    return render(request, 'test.html', context)


def home_view(request, pk):
    # qs = Store.objects.get(id=id)
    try:
        qs = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404  # render a HTML page with a status code of 404
    return HttpResponse(f'Store ID : {qs.pk}')


def home_api_view(request, pk):
    try:
        qs = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        # return a JSON with a status code of 404
        return JsonResponse({'message': 'Not Found'})
    return JsonResponse({'pk': qs.pk})


class PostListView(ListView):
    model = Store
    template_name = 'retailstores/store_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'store'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Store
    template_name = 'retailstores/store_single.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'i'


class UserPostListView(ListView):
    model = Store
    template_name = 'retailstores/my_store.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'store'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Store.objects.filter(user=user).order_by('-created_at')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Store
    template_name = 'retailstores/add_store.html'  # <app>/<model>_<viewtype>.html

    fields = ['name', 'description', 'cover_image',
              'categories', 'url', 'mon_start', 'mon_end', 'tue_start',
              'tue_end', 'wed_start', 'wed_end', 'thu_start', 'thu_end',
              'fri_start', 'fri_end', 'sat_start', 'sat_end', 'sun_start',
              'sun_end', 'photo_1', 'photo_2', 'photo_3']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['name', 'description', 'cover_image',
              'categories', 'url', 'mon_start', 'mon_end', 'tue_start',
              'tue_end', 'wed_start', 'wed_end', 'thu_start', 'thu_end',
              'fri_start', 'fri_end', 'sat_start', 'sat_end', 'sun_start',
              'sun_end', 'photo_1', 'photo_2', 'photo_3']
    redirect_url = 'retailstore:my_store'
    context_object_name = 'store'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        store = self.get_object()
        if self.request.user == store.user:
            return True
        return False

# def store(request):
#     return render(request, 'retailstores/add_store.html', {})


# def my_store(request, user):
#     store = Store.objects.filter(user__username=request.user)
#     print(store)
#     context = {'store': store}
#     return render(request, 'retailstores/store_single.html', context)


# def store_view(request, *args, **kwargs):
#     store = Store.objects.all()
#     for i in store:
#         if request.user == i.user:
#             print(i.slug)
#             print(i.categories)

#     context = {'store': store}
#     return render(request, 'retailstores/view_store.html', context)


# def store_single(request, slug):
#     store = Store.objects.filter(slug=slug)
#     context = {'store': store}
#     return render(request, 'retailstores/store_single.html', context)
