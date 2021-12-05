from api.model.area import Area
from api.model.college import College
from api.service.iterate import *


class DataRepository:

    area = [
        Area(1,"Area Administrativa"),
        Area(2,"Area Socio-Humanística"),
        Area(3,"Area Técnica"),
        Area(4,"Area Biológica"),
    ]

    college = [
        College(1,"FACULTAD DE CIENCIAS SOCIALES, EDUCACIÓN Y HUMANIDADES", 2),
        College(2,"FACULTAD DE CIENCIAS EXACTAS Y NATURALES", 3),
        College(3,"FACULTAD DE CIENCIAS DE LA SALUD", 4),
        College(4,"FACULTAD DE CIENCIAS ECONÓMICAS Y EMPRESARIALES", 1),
        College(5,"FACULTAD DE INGENIERIAS Y ARQUITECTURA", 3),
        College(6,"FACULTAD DE CIENCIAS JURÍDICAS Y POLÍTICAS", 1),
    ]

    object_area = []

    def get_all_areas(self,request):
        object_area = generate_compiled_area(self.area,self.college,request)
        return object_area

    def search_area_by_pos(self, pos, request):
        object_area = generate_area_pos(self.area,self.college,request)
        pos -= 1
        if 0 <= pos < len(object_area):
            return object_area[pos]
        return None

    def search_college_by_area(self,pos,request):
        object_area = generate_college_area(self.area,self.college,request)
        pos -= 1
        if 0 <= pos < len(object_area):
            return list(object_area[pos].college)
        return None

    