from django.views.generic import DetailView, ListView
from .models import Fighter
from blog.views import BaseMixin


class FighterListView(ListView, BaseMixin):
    template_name = 'fighters/fighter.html'
    context_object_name = 'fighters'
    paginate_by = 6
    model = Fighter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'Fighters'
        context.update(self.context)
        return context


class FighterDetailView(BaseMixin, DetailView):
    template_name = 'fighters/single-fighter.html'
    context_object_name = 'fighter'
    slug_url_kwarg = 'fighter_slug'
    model = Fighter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        return context
