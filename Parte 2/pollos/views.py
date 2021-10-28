# from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from pollos.models import Pollo


def get_view_context():
    col_names = [field.name for field in Pollo._meta.get_fields()][1:]

    unique_lesiones = Pollo.objects.order_by().values_list('lesionTipo').distinct()
    unique_granjas = Pollo.objects.order_by().values_list('granja').distinct()

    unique_lesiones = [lesion[0] for lesion in unique_lesiones]
    unique_granjas = [granja[0] for granja in unique_granjas]

    return col_names, unique_lesiones, unique_granjas

def pollos_api(request):
    """Get_Params: page, lowest_date, highest_date, lesionTipos, granjas"""

    # Define Get Params

    lowest_date = request.GET.get('lowest_date')
    highest_date = request.GET.get('highest_date')
    page_number = request.GET.get('page')
    lesionTipos = request.GET.getlist('lesionTipos')
    granjas = request.GET.getlist('granjas')

    query_dates = Q()
    query_lesion = Q()
    query_granja = Q()
    print(lowest_date)
    if lowest_date:
        query_dates.add(Q(fecha__gte=lowest_date), Q.AND)
    if highest_date:
        query_dates.add(Q(fecha__lte=highest_date), Q.AND)

    if lesionTipos:
        for lesionTipo in lesionTipos:
            query_lesion.add(Q(lesionTipo__contains=lesionTipo), Q.OR)
    if granjas:
        for granja in granjas:
            query_granja.add(Q(granja__contains=granja), Q.OR)
        pass

    pollos = Pollo.objects.filter(
        query_dates & query_lesion & query_granja
        ).order_by('id')

    # Pagination
    paginator = Paginator(pollos, 10)
    pollos_page = paginator.get_page(page_number)

    col_names, unique_lesiones, unique_granjas = get_view_context()

    return render(
        request, 'index.html',
        {
            'pollos': pollos_page,
            'col_names': col_names,
            'unique_lesiones': unique_lesiones,
            'unique_granjas': unique_granjas,
            'lowest_date': lowest_date if lowest_date else '2020-01-15',
            'highest_date': highest_date if highest_date else '2020-12-30',
            'lesionTipos' : lesionTipos if lesionTipos else None,
            'granjas' : granjas if granjas else None,
        }
    )
