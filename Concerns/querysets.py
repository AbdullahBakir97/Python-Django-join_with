from django.db.models import QuerySet, Count, Prefetch

class JoinWithQuerySet(QuerySet):
    def filter_by_status(self, status):
        return self.filter(status=status)

    def filter_by_country(self, country_name):
        return self.filter(profile__country__name=country_name)
    
    def annotate_profile_count(self):
        return self.annotate(profile_count=Count('profile'))

    def annotate_order_count(self):
        return self.annotate(order_count=Count('order'))
    
    def join_with_profile(self):
        return self.select_related('profile')

    def join_with_order_status(self, status):
        return self.filter(order__status=status).distinct()
    
    def join_with(self, *relations, **kwargs):
        try:
            queryset = self
            if relations:
                queryset = queryset.select_related(*relations)
            if kwargs:
                prefetch_objects = [Prefetch(key, value) for key, value in kwargs.items()]
                queryset = queryset.prefetch_related(*prefetch_objects)
            return queryset
        except Exception as e:
            raise ValueError(f"Error performing join_with: {str(e)}")
