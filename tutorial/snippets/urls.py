from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# ルーターを作成し、ViewSet をそのルーターに登録します。
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# これにより、APIのURLはルーターによって自動的に決定されます。
urlpatterns = [
    path('', include(router.urls)),
]
