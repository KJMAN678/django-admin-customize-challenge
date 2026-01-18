from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# ヘッダーのタイトル
admin.site.site_header = "システム管理者用サイト"
# タブのタイトル
admin.site.site_title = "マイプロジェクト"
# インデックスページのタイトル
admin.site.index_title = "ホーム"

# サイトを表示、を非表示にできる
admin.site.site_url = None


def has_permission(request):
    return request.user.is_active


# 管理者サイトにアクセスするための条件
admin.site.has_permission = has_permission

urlpatterns = [
    path("admin/", admin.site.urls),
    path("web/", include("web.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
