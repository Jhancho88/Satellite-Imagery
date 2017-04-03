imagery_repository = 'C:/Orunmila/IMAGERY'
satellite = 'LANDSAT_8'
tile = '005087'
scene = 'LC80070592017018LGN00'
band_list = ['1', '2', '3']

stack_list = []

for band in band_list:
    path = '{0}/{1}/{2}/{3}/{4}_B{5}.TIF'.format(imagery_repository, satellite, tile, scene, scene, band)
    stack_list.append(path)

print stack_list


