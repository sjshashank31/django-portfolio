from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import socket

socket.getaddrinfo('127.0.0.1', 8080)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>')



