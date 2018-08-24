from gmplot import gmplot

# Place map
#gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)
gmap = gmplot.GoogleMapPlotter(41.5711478, -87.574017, 13)
'''# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)'''

# Test circles from untappd
drink_lats, drink_lons = zip(*[
    (41.4791753,-87.9575961),
    (41.4449186,-87.632487),
    (44.0050795,-86.4710219),
    (41.5711478,-87.574017),
    (41.5433162,-87.6808406),
    (41.5570015,-87.6709024)
    ])
gmap.scatter(drink_lats, drink_lons, '#3B0B39', size=10000, marker=False)
    
# Scatter points
'''top_attraction_lats, top_attraction_lons = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)
'''

# Marker
hidden_gem_lat, hidden_gem_lon = 41.5711478,-87.574017
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")
