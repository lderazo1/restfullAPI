relations = ['self','college','area']

def get_areas(area,college):
    temp = []
    for areas in area:
        areas.college = [element for element in college if element.area == areas.id]
        temp.append(areas)
    return temp

def generate_compiled_area(area,college, request):
    temp = get_areas(area,college)
    object = compile_link(relations,temp,request)     
    return temp

def generate_college_area(area,college, request):
    temp = temp = get_areas(area,college)
    object = compile_area_link(relations,temp,request)  
    return temp

def generate_area_pos(area,college, request):
    temp = temp = get_areas(area,college)
    object = compile_area(relations,temp,request)  
    return temp

def compile_link(relations, temp, request):
    object = []
    for i in temp:
        i.rel = relations[0]
        i.href = request.url+'/'+str(i.id)
        i.method = 'GET'
        for j in i.college:
            j.rel = relations[1]
            j.href = request.url+'/'+str(i.id)+'/college'
            j.method = 'GET'

    return object

def compile_area_link(relations, temp, request):
    object = []
    for i in temp:
        i.rel = relations[0]
        i.href = request.url+'/'+str(i.id)
        i.method = 'GET'
        for j in i.college:
            j.rel = relations[1]
            j.href = request.url
            j.method = 'GET'

    return object

def compile_area(relations, temp, request):
    object = []
    for i in temp:
        i.rel = relations[0]
        i.href = request.url_root+'area'
        i.method = 'GET'
        for j in i.college:
            j.rel = relations[1]
            j.href = request.url+'/college'
            j.method = 'GET'

    return object