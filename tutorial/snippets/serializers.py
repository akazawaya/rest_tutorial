from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        バリデーションが通ったデータをもとに、新しいSnippetインスタンスを作成して返します。
        ** は辞書のアンパック…複数の変数や引数に一度に展開する
        この場合 A:aa という辞書要素に対し、A=aa を展開
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        バリデーションが通ったデータをもとに、既存のSnippetインスタンスを更新して返します。
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
