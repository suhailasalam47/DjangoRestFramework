from dataclasses import field
from rest_framework import serializers
from movielist.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # exclude = ['active']

    def get_len_name(self, object):
        return len(object.name)
        
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should not be same")
        else:
            return data

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