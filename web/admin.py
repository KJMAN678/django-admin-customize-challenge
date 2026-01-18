from django.contrib import admin

from .forms import AuthorAdminForm
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    # 簡易検索
    search_fields = ["name"]

    # サイドバーのフィルター
    list_filter = ["email"]

    # アクション一覧
    actions = ["clear_name"]

    # 登録・編集画面のフォームの機能を上書きする
    form = AuthorAdminForm

    @admin.action(
        description="名前をクリアする",
        permissions=[
            "change",
        ],
    )
    def clear_name(self, request, queryset):
        """Authorモデルの名前を空白にする"""
        queryset.update(name="")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
