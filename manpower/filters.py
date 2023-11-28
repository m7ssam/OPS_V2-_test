from django_filters import FilterSet, DateFilter, CharFilter
from .models import Mp_list

class Mp_list_Filter(FilterSet):
  # start_date = DateFilter(field_name = "hire", lookup_expr='gte')
  # end_date = DateFilter(field_name = "hire", lookup_expr='lte')
  class Meta:
    model = Mp_list
    fields = ["id", "full_name", "contract", "code__job","code__speciality", "code__dep"]