from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
	"""
	adding endpoints for our user models 
	and reflect the owner-snippets-reation
	"""
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
	"""
	adding endpoints for our user models 
	"""
	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')
						