from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PaginationMovie(PageNumberPagination):
    page_size = 3


class MovieLOPagination(LimitOffsetPagination):
    default_limit = 4