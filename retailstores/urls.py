from django.urls import path
from . import views

app_name = 'retailstore'

urlpatterns = [
    path('test/',views.test),
    path('home_view/<int:pk>/', views.home_view),
    path('api/home_view/<int:pk>/', views.home_api_view),
    path('', views.PostListView.as_view(), name='store'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='my_store'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='store_single'),
    path('post/new/', views.PostCreateView.as_view(), name='add_store'),
    path('post/<int:pk>/update/',
         views.PostUpdateView.as_view(), name='store-update'),

    #     path('', views.PostListView.as_view(), name='store'),
    #     path('add_store/new/', views.PostCreateView.as_view(), name='add_store'),
    #     path('post/<str:username>/update/',
    #          views.PostUpdateView.as_view(), name='store-update'),
    #     path('post/<str:username>/', views.PostDetailView.as_view(), name='store_single'),
    #     path('my_store/<str:username>',
    #          views.UserPostListView.as_view(), name='my_store'),

    # path('add_store', views.store, name='add_store'),
    # path('all_store/', views.store_view, name='all_stores'),
    # path('my_store/<str:user>/', views.my_store, name='my_store'),

    # path('all_store/<slug>', views.store_single, name='store_single'),

]
