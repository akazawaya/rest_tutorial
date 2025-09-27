from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # 表示用の“シリアライズ項目”を定義しているだけで,モデル（DBスキーマ）に変更はない
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner', 'style', 'highlight', 'title', 'code', 'linenos', 'language']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']