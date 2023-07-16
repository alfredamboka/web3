import os
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand
from schools.models import School


class Command(BaseCommand):
    help = 'Loads schools from GeoJSON file into the database'

    def handle(self, *args, **options):
        geojson_file = 'schools/Data/Schools.geojson'
        mapping = {
            'OBJECTID': 'properties.OBJECTID',
            'CODE': 'properties.CODE',
            'SCHOOL_NAM': 'properties.SCHOOL_NAM',
            'LEVEL': 'properties.LEVEL',
            'Status': 'properties.Status',
            'County': 'properties.County',
            'District': 'properties.District',
            'ZONE': 'properties.ZONE',
            'SUBCOUNTY': 'properties.SUBCOUNTY',
            'Ward': 'properties.Ward',
            'X_Coord': 'properties.X_Coord',
            'Y_Coord': 'properties.Y_Coord',
            'Source': 'properties.Source',
        }

        with open(geojson_file) as f:
            data = json.load(f)

        features = data['features']
        for feature in features:
            properties = feature['properties']
            geometry = feature['geometry']
            x_coord = properties.get('X_Coord')
            y_coord = properties.get('Y_Coord')
            if x_coord and y_coord:
                location = Point(float(x_coord), float(y_coord))
                School.objects.create(location=location,
                                      **{mapping[field]: value for field, value in properties.items() if
                                         field in mapping})
