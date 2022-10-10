from dataclasses import fields
from platform import platform
from rest_framework import serializers
from movielist.models import WatchList, StreamPlatform, Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    # review = ReviewsSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['active']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
       
        


    # def get_len_name(self, object):
    #     return len(object.name)
        
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description should not be same")
    #     else:
    #         return data

# def validate_name( value):
#         if len(value)<3:
#             raise serializers.ValidationError("Name must have atleast 3 characters")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description should not be same")
    #     else:
    #         return data