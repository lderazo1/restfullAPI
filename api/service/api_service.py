from api.enconde import EmployeeEncoder
from api.database.data_repository import DataRepository
from flask import abort, request
from flask_negotiate import consumes, produces
from api.service import blueprint
import json

data_repository = DataRepository()


@blueprint.route('/')
def index():
    return "Prueba Segundo Parcial"


@blueprint.route('/area', methods=['GET'])
@produces('application/json')
def get_area():
    area = data_repository.get_all_areas(request)
    if area:
        return json.dumps(area, cls=EmployeeEncoder), 200
    abort(404)

@blueprint.route('/area/<int:pos>', methods=['GET'])
@produces('application/json')
def get_area_by_pos(pos):
    area = data_repository.search_area_by_pos(pos,request)
    if area:
        return json.dumps(area, cls=EmployeeEncoder), 200
    abort(404)

@blueprint.route('/area/<int:pos>/college', methods=['GET'])
@produces('application/json')
def get_college_by_area(pos):
    college = data_repository.search_college_by_area(pos,request)
    if college:
        return json.dumps(college, cls=EmployeeEncoder), 200
    abort(404)