from rest_framework import serializers
from app.models import User,Category,Book


class UserRegistrationSerializer(serializers.ModelSerializer):

  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email', 'name', 'password', 'password2', 'tc']
    extra_kwargs={
      'password':{'write_only':True}
    }


  def validate(self, data):
    password = data.get('password')
    password2 = data.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return data

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'author', 'category_name']

class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  

    class Meta:
        model = Category
        fields = ['name', 'books']

class UserProfileSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)  
    class Meta:
        model = User  
        fields = ['id', 'name', 'email', 'categories']  
