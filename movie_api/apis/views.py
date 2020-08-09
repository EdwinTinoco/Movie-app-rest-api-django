from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apis.models import Movies

class MovieList(APIView):
   def get(self, request):
      cursor = connection.cursor()
      cursor.callproc("spGetAllMovies", ())

      columns = [column[0] for column in cursor.description]
      movies = []
      for row in cursor.fetchall():
         movies.append(dict(zip(columns, row)))    

      cursor.close()
      return Response(movies)
      

   def post(self, request):
      title = request.data['title']
      description = request.data['description']
      genre = request.data['genre']
      image_url = request.data['image_url']
      year_release = request.data['year_release']
      classification = request.data['classification']
      duration = request.data['duration']

      cursor = connection.cursor()
      cursor.callproc("spInsertMovie", [title, description, genre,
      image_url, year_release, classification, duration])

      connection.commit()
      cursor.close()
      return Response('Movie added succesfully!')



class MovieDetail(APIView):      
   def get(self, request, pk):
      cursor = connection.cursor()
      cursor.callproc("spGetMovieById", [pk])

      columns = [column[0] for column in cursor.description]
      movie = []
      for row in cursor.fetchall():
         movie.append(dict(zip(columns, row))) 

      cursor.close()
      return Response(movie)


   def put(self, request, pk):
      title = request.data['title']
      description = request.data['description']
      genre = request.data['genre']
      image_url = request.data['image_url']
      year_release = request.data['year_release']
      classification = request.data['classification']
      duration = request.data['duration']

      cursor = connection.cursor()
      cursor.callproc("spUpdateMovieById", [pk, title, description, genre,
      image_url, year_release, classification, duration])

      connection.commit()
      cursor.close() 
      return Response("Movie info updated successfully!")


   def delete(self, request, pk):
      cursor = connection.cursor()
      cursor.callproc("spDeleteMovieById", [pk])
      connection.commit()
      cursor.close()

      return Response("Movie deleted successfully")


class MovieComments(APIView):      
   def get(self, request, pk):
      cursor = connection.cursor()
      cursor.callproc("spGetCommentsByMovieId", [pk])

      columns = [column[0] for column in cursor.description]
      comments = []
      for row in cursor.fetchall():
         comments.append(dict(zip(columns, row))) 

      cursor.close()
      return Response(comments)


class MovieAddComment(APIView):  
   def post(self, request):
      comment = request.data['comment']      
      created = request.data['created']      
      movie_id = request.data['movie_id']      
      user_id = request.data['user_id']      

      cursor = connection.cursor()
      cursor.callproc("spInsertComment", [comment, created, movie_id, user_id])

      connection.commit()
      cursor.close()
      return Response('Comment added succesfully!')


class MovieAddRate(APIView):  
   def post(self, request):
      rated = request.data['rated']      
      movie_id = request.data['movie_id']    

      cursor = connection.cursor()
      cursor.callproc("spInsertRatedByMovieId", [rated, movie_id])

      connection.commit()
      cursor.close()
      return Response('Rate added succesfully!')


class MovieTotalUsersRateMovie(APIView):      
   def get(self, request, pk):
      cursor = connection.cursor()
      cursor.callproc("spGetTotalUsersRateMovie", [pk])
      rates = cursor.fetchall()

      cursor.close()
      return Response(rates)


class UserLogin(APIView):  
   def post(self, request):
      email = request.data['email']      
      passw = request.data['passw']    

      cursor = connection.cursor()
      cursor.callproc("spCheckUserLogin", [email, passw])

      columns = [column[0] for column in cursor.description]
      user = []
      for row in cursor.fetchall():
         user.append(dict(zip(columns, row))) 

      cursor.close()
      return Response(user)

class UserSignUp(APIView): 
   def post(self, request):
      name = request.data['name']      
      email = request.data['email']      
      passw = request.data['password']    

      cursor = connection.cursor()
      cursor.callproc("spInsertUser", [name, email, passw])

      connection.commit()
      cursor.close()
      return Response('User added succesfully!')

class UserLastId(APIView):      
   def get(self, request):
      cursor = connection.cursor()
      cursor.callproc("spGetIdLastUser", ())
      user = cursor.fetchall()

      cursor.close()
      return Response(user)


class UserId(APIView): 
   def get(self, request, pk):
      cursor = connection.cursor()
      cursor.callproc("spGetUserById", [pk])

      columns = [column[0] for column in cursor.description]
      user = []
      for row in cursor.fetchall():
         user.append(dict(zip(columns, row))) 

      cursor.close()
      return Response(user)