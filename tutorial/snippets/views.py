from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework import viewsets

class SnippetViewSet(viewsets.ModelViewSet):
    """
    この ViewSet は、自動的に list、create、retrieve、update、および destroy の各操作を提供します。

    さらに、追加で highlight 操作も提供しています。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    このViewSetは自動的に list と retrieve の操作を提供します。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
