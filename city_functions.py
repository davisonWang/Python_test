###   动手试一试

def get_formatted_name(city, country, population=''):
    if population:
        city_full_name = city + ' ' + country + ' ' + population
        return city_full_name.title()
    else:
        city_full_name = city + ' ' + country
        return city_full_name.title()



