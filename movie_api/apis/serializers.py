from rest_framework import serializers
from apis.models import Movies
from apis.models import Comments
from apis.models import Rates

class MoviesSerializer(serializers.ModelSerializer):
   class Meta:
      model = Movies
      # fields = '__all__'
      fields = ['id', 'title', 'description', 'genre', 'image_url', 'year_release', 'classification', 'duration', 'ratings', 'rated']   

   def create(self, validated_data):
      return Movies.objects.create(**validated_data)

   def update(self, instance, validated_data):
      instance.title = validated_data.get('title', instance.title)
      instance.description = validated_data.get('description', instance.description)
      instance.genre = validated_data.get('genre', instance.genre)
      instance.image_url = validated_data.get('image_url', instance.image_url)
      instance.year_release = validated_data.get('year_release', instance.year_release)
      instance.classification = validated_data.get('classification', instance.classification)
      instance.duration = validated_data.get('duration', instance.duration)
      instance.ratings = validated_data.get('ratings', instance.ratings)
      instance.rated = validated_data.get('rated', instance.rated)

      instance.save()
      return instance
      

class CommentsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Comments
      fields = '__all__'  

   def create(self, validated_data):
      return Comments.objects.create(**validated_data)

   def update(self, instance, validated_data):
      instance.comment = validated_data.get('comment', instance.comment)
      instance.created = validated_data.get('created', instance.created)
      instance.movie_id = validated_data.get('movie_id', instance.movie_id)
      instance.user_id = validated_data.get('user_id', instance.user_id)      

      instance.save()
      return instance


class RatesSerializer(serializers.ModelSerializer):
   class Meta:
      model = Rates
      fields = '__all__'  

   def create(self, validated_data):
      return Rates.objects.create(**validated_data)

   def update(self, instance, validated_data):
      instance.rated = validated_data.get('rated', instance.rated)
      instance.movie_id = validated_data.get('movie_id', instance.movie_id)
      instance.user_id = validated_data.get('user_id', instance.user_id)      

      instance.save()
      return instance



