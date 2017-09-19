import folium #for maps
import pandas #for reading files
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"]) #set lat to list of column LAT
lon=list(data["LON"]) #set lon to list of column LON
elev=list(data["ELEV"])
def color_producer(elevation ):
	if elevation < 1000:
		return 'green'
	elif 1000<=elevation <3000:
		return 'orange'
	else:
		return 'red'

map=folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="MApbox Bright")  #location in latitude and longitude
fgv=folium.FeatureGroup(name="Volcanoes") # feature group for maps to make code neater(Volcanoes)
#for coordinates in [[8.45, -5.7 ], [9.7, -6.7]]:
for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))
	#removed from above line: icon=folium.Icon(color=color_producer(el))
fgp=folium.FeatureGroup(name="Population") #feature group for Population

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),  
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 #lambda
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) #for json data,

map.add_child(fgv) #add feature to map
map.add_child(fgp) #add feature to map
map.add_child(folium.LayerControl())
map.save("BeninMap1.html") #save map to file
