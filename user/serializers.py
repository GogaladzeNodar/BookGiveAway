from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
# es serialaizeri imitom gvchirdeba rom registraciis serialaizerit ar gamodis. vfiqrob unikalurobis gamo
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
