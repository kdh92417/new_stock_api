from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password
from account.models import User


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    fullname = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    phone_number = serializers.CharField(write_only=True, required=True)
    birth_date = serializers.DateField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'password', 'password2',
                  'email', 'phone_number', 'birth_date')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.fullname = validated_data.get('fullname', instance.fullname)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone_number = validated_data.get(
    #         'phone_number', instance.phone_number)
    #     instance.birth_date = validated_data.get(
    #         'birth_date', instance.birth_date)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            birth_date=validated_data['birth_date'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'fullname', 'password', 'email',
                  'phone_number', 'birth_date', 'portfolio']
