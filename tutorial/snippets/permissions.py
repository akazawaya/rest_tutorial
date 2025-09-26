from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    オブジェクトの所有者のみが編集できるようにするカスタムパーミッション。
    """

    def has_object_permission(self, request, view, obj):
        # 読み取りパーミッションはすべてのリクエストに許可されます。
        # したがって、GET、HEAD、OPTIONS リクエストは常に許可されます。
        if request.method in permissions.SAFE_METHODS:
            return True

        # 書き込みパーミッションはスニペットの所有者にのみ許可されます。
        return obj.owner == request.user
