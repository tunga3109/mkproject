from django.contrib import admin
from django.forms import ModelForm

from .models import Category, Comment, Post, Contact
from fighters.models import Fighter


@admin.action(description='опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


class ManagerPanel(admin.AdminSite):
    site_header = 'Manager Panel'
    site_title = 'manager'
    index_title = 'manager index'


manager = ManagerPanel(name='manager')


class PostInline(admin.StackedInline):
    model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    inlines = (PostInline,)
    list_display = ('id', 'name', 'is_published')
    list_editable = ('name',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'descr')
    search_help_text = 'Поиск по заголовку'
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('date_created',)
    date_hierarchy = 'date_created'
    ordering = ('date_created', '-title')
    list_display = ('title', 'full_name', 'date')
    list_filter = ('is_published', 'category', 'date_created')
    fieldsets = (
        (
            'Основное',
            {
                'fields': ('title', 'descr', 'category'),
                'description': 'Основные значения'
            }
        ),
        (
            'Дополнительное',
            {
                'fields': ('date_created', 'author', 'slug', 'image')
            }
        )
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


class ContactManager(ContactAdmin):
    readonly_fields = ('email', 'name', 'message', 'date_created')


@admin.register(Fighter)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['character_name']
    prepopulated_fields = {'slug': ('character_name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('post', 'namer', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



manager.register(Category, CategoryAdmin)
manager.register(Post, PostAdmin)
manager.register(Contact, ContactManager)
manager.register(Comment, CommentAdmin)

