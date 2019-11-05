color_red = (255,0,0)
r,g,b = color_red

print(r)

print(color_red[0])

color_light_red = list(color_red)
color_light_red[0] = 250
color_light_red = tuple(color_light_red)
print(color_light_red)
