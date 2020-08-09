from django.urls import path
from apis import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('api/movies/', views.MovieList.as_view()),
   path('api/movies/<int:pk>/', views.MovieDetail.as_view()),
   path('api/movies/comments/<int:pk>/', views.MovieComments.as_view()),
   path('api/movies/comments/', views.MovieAddComment.as_view()),
   path('api/movies/rates/', views.MovieAddRate.as_view()),
   path('api/movies/rates/<int:pk>', views.MovieTotalUsersRateMovie.as_view()),
   path('api/users/login/', views.UserLogin.as_view()),
   path('api/users/signup/', views.UserSignUp.as_view()),
   path('api/users/id/', views.UserLastId.as_view()),
   path('api/users/<int:pk>/', views.UserId.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
