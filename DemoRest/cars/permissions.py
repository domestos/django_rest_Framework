from rest_framework import permissions
# наслідуємося від базового класу
class IsOwnerOrReadOnly(permissions.BasePermission):
    # переоприділяємо його метод
    def has_object_premission(self, request, view, obj):
        #  якщо метод запросу рівний безпечному запросу  SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') то повертаємо True
        if request.method in permissions.SAFE_METHODS:
            return True
        # якщо метод запросу не є безпченим, то повертається резкльта перевірки юзера
        return obj.user == request.user
