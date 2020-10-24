from django.urls import path, include

app_name = 'api/v1'

urlpatterns = [
    path('', include(router.urls)),
    path('favorite/create', FavoriteCreateView.as_view(), name='car_list'),
    path('favorite/delete', FavoriteDeleteView.as_view(), name='car_detail'),

    # path('new_posts/', SendNewPostsView.as_view(), name='post_send')
]