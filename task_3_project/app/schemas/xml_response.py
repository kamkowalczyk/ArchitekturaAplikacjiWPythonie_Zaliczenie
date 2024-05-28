from fastapi.responses import Response
from dicttoxml import dicttoxml

def xml_response(data):
    xml_data = dicttoxml(data.__dict__, custom_root='order', attr_type=False)
    return Response(content=xml_data, media_type="application/xml")
