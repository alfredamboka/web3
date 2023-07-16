from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from .models import School


def school_map(request):
    return render(request, 'schools/map.html')


def get_schools(request):
    county = request.GET.get('county')
    school_name = request.GET.get('school_name')
    district = request.GET.get('district')

    queryset = School.objects.all()

    if county:
        queryset = queryset.filter(County=county)
    if school_name:
        queryset = queryset.filter(SCHOOL_NAM__icontains=school_name)
    if district:
        queryset = queryset.filter(District=district)

    schools_geojson = serialize('geojson', queryset, geometry_field='location')

    return JsonResponse(schools_geojson, safe=False)


def get_school(request, school_id):
    school = School.objects.get(id=school_id)
    school_geojson = serialize('geojson', [school], geometry_field='location')

    return JsonResponse(school_geojson, safe=False)
