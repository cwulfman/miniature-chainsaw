from rdflib import Graph


harvard_url = "https://iiif.harvardartmuseums.org/manifests/object/292449"
tufts_url = "https://dl.tufts.edu/concern/images/9s161915g/manifest"

g = Graph()
g.parse(tufts_url, format='json-ld')
# g.serialize(destination="/tmp/o.ttl")

q = """select * where 
{?image a dctypes:Image ;
        dc:format ?format ;
        svcs:has_service ?svcs ;
        exif:height ?height ;
        exif:width ?width .

}
"""


result = g.query(q)