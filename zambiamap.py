#!/usr/bin/env python
import mapnik 
mapfile = '/usr/share/webmaps/zambia-all-linux.xml'
map_output = '/var/www/html/maps/map_of_zambia.png'
m = mapnik.Map(1200, 900)
mapnik.load_map(m, mapfile)
m.zoom_all()
#bbox = mapnik.Envelope(mapnik.Coord(21.7529, -18.271), mapnik.Coord(33.9697, -7.8416))
#m.zoom_to_box(bbox)
mapnik.render_to_file(m, map_output)