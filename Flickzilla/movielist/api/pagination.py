from rest_framework.pagination import PageNumberPagination


class PaginationMovie(PageNumberPagination):
    page_size = 3