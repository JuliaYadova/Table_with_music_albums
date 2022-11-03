from django_filters.rest_framework import FilterSet, filters

from .models import Album


class CustomOrderingFilterSet(FilterSet):
    """Сортировка согласно ТЗ.
    В классе создается сортировка по запросу '.../?sorting=<fields>',
    согласно ТЗ поле связанной модели передается через @.
    """
    sorting = filters.OrderingFilter(fields=(
            ('name', 'name'),
            ('artist', 'artist@name'),
        ),)

    class Meta:
        model = Album
        fields = ('sorting',)
