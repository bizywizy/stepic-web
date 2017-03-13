from django.core.paginator import Paginator, EmptyPage
from django.http import Http404


def paginate(request, qs):
    LIMIT = 10

    try:
        page_num = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, LIMIT)
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
