# map
# Определим функцию, которая будет переводить МИли в километры
print('map    Определим функцию, которая будет переводить МИли в километры')

def miles_to_km(miles):
    return miles * 1.6
mile_dist = [1.0, 1.6, 2.3]


km_dist = list(map(miles_to_km, mile_dist)) # list  потому что map возвр-ет свой спецефич. тип
print((type(km_dist), km_dist))