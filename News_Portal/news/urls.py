from django.urls import path
# Импортируем созданное нами представление
from .views import (PostList,
                    PostDetail,
                    PostSearchView,
                    NewsCreate,
                    ArticlesCreate,
                    NewsEdit,
                    ArticlesEdit,
                    NewsDelete,
                    ArticlesDelete,
                    PostAuthorView,
                    sub_cat,
                    un_sub_cat,
                    CategoryList,
                    )


urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostList.as_view(), name='posts_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('news/<int:pk>/edit', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/edit', ArticlesEdit.as_view(),
         name='articles_edit'),
    path('articles/<int:pk>/delete', ArticlesDelete.as_view(),
         name='articles_delete'),
    path('my_posts/', PostAuthorView.as_view(), name='post_author_view'),
    path('sub_cat/category/<int:pk>', sub_cat, name='sub_cat'),
    path('un_sub_cat/category/<int:pk>', un_sub_cat, name='un_sub_cat'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
]
