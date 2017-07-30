from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	"""
	adding endpoints for our user models 
	and reflect the owner-snippets-reation
	(rewritten to hyperlinking our API)
	"""
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	adding endpoints for our user models 
	"""
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'snippets')
						