#Folium
#to create a web map, we cannot do it directly with python
#we use folium here to convert our python code automatically to javascript,html and css
#In other words, folium will use the data strengths from python and mapping strengths
#from leaflet.js library and use that data we provided with the help of python and then
#visualizes it in a leaflet map.

#importing the folium library
import folium
#impoting the pandas library
import pandas

#we are importing the statesinfo.csv file to a variable called data using pandas read_csv method
data = pandas.read_csv('statesinfo.csv')

#here,we are importing each individual coloumn from statesinfo (data variable) and converting them into a list
#and storing them in a variable name related to the coloumn for further purpose
statee = list(data['state'])
capitall = list(data['capital'])
latitude = list(data['lat'])
longitude = list(data['long'])
populationn = list(data['population'])
img = list(data['imgsrc'])

#we need to create a map object from a map class,we need this map object to do any operations for maps usually to Create a base Map with Folium and Leaflet.js
#Map class has the following parameters as input
#Map(locationn=None, width='100%', height='100%', left='0%', top='0%', position='relative',
#tiles='OpenStreetMap', attr=None, min_zoom=0, max_zoom=18, zoom_start=10, min_lat=-90,
# max_lat=90, min_lon=-180, max_lon=180, max_bounds=False, crs='EPSG3857', control_scale=False,
# prefer_canvas=False, no_touch=False, disable_3d=False, png_enabled=False, zoom_control=True, **kwargs)
#the location parameter here refers to the location which you want to see when you run this file on browser
map = folium.Map(location=[23.733058,78.070710],zoom_start=4.5,tiles="OpenStreetMap")
#here,i created a feature_group variable which has the FeatureGroup layer class that takes the following parameters
#FeatureGroup(name=None, overlay=True, control=True, show=True, **kwargs)
#Create a FeatureGroup layer ; you can put things in it and handle them as a single layer.
feature_group = folium.FeatureGroup(name='Population')
#the map object we have created above will only create a base map of world simply with no borders
#here we are importing the geojson data set of india, which is a polygon set of data of eash state boundaries in json format
#this data set provides all the states borders in the form of polygon layer
#the below code will not only add the imported borders but also uses the style_function parameter to
#show population status of each status in 3 different colors
#we are passng a data parameter which imports that dataset
#we use style_function parameter which expects an anonymous function called lambda function
feature_group.add_child(folium.GeoJson(data=open('india.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {
                                                                                                                          #fillcolor : red if the population in a state is more
                                                                                                                          #than 50000000
                                                                                                                          'fillColor':'red'
                                                                                                                          if x['properties']['pop'] > 50000000
                                                                                                                          # : yellow if the population in a state is more than
                                                                                                                          #30000000 and less than 50000000
                                                                                                                          else 'yellow' if 50000000 >= x['properties']['pop'] > 30000000
                                                                                                                          #if not both the above, then fillcolor with green
                                                                                                                          else 'green'
                                                                                                                        }
                                       )
                        )
#here, we are using zip() method so that all the list items get together instead of being seperate or it zips the data in various lists together
#and i have created a individual variable for each list item as shown below
#for every iteration,the below variables will take the values from the zip(variables) and store in them to use in loop
for _state,_capital,_latitude,_longitude,_population,_img in zip(statee,capitall,latitude,longitude,populationn,img):
    # here we are adding a CircleMarker as child to our feature group,this adds a circle type of marker to the base map
    # we can add multiple markers to multiple points using this for loop
    #the CircleMarker will take all the below inputs as shown below
    feature_group.add_child(folium.CircleMarker(#location parameter takes both lat and long as input and places circle marker there
                                                location=[_latitude,_longitude],
                                                #radius of circle marker
                                                radius=5,
                                                #popup occurs when you click on tooltip,this can be a html
                                                popup=f'<p><strong>State: </strong>{_state}</br><strong>Capital: </strong>{_capital}</br><strong>Population: </strong>{_population}</p><img src={_img} width="160px" height="110px">',
                                                #tooltip occurs when you hover on a marker
                                                tooltip=_state,
                                                color='#660000',
                                                fill_color = '#b30000',
                                                fill = True,
                                                fill_opacity=0.6))
#after adding all the necessary things to a feature group, like marker,polygon layer etc etc we will then add that feature group
#to the base map object
map.add_child(feature_group)
#save method is used to save our map we created in html format
map.save('MyWebMap.html')













































