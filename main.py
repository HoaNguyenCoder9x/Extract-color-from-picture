import colorgram

picture = 'colorful.jpg'
numbers_of_color_to_extract = 9
color = colorgram.extract(picture, numbers_of_color_to_extract)
color_list = []
for i in color:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)
print(color_list)

