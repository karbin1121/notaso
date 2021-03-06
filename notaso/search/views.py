from django.views.generic import ListView

from ..professors.models import Professor


class SearchView(ListView):
    queryset = Professor.objects.all().order_by("-first_name", "last_name")
    template_name = "search.html"

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        context.update(
            {"search_term": self.request.GET.get("q", ""), "navbarSearchShow": True}
        )

        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_term = self.request.GET.get("q")

        if search_term:
            for term in search_term.split():
                qs = Professor.objects.search(term, raw=True)
            return qs

        return queryset[:10]
