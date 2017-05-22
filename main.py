from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='templates/home.jinja2'
)
def hello_world(request):
    css_url = request.static_url('static/css/mine.css')
    v = {
        'h1': 'HEADER1',
        'h2': 'HEADER2',
        'css': css_url,
    }
    return v


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_static_view(name='static', path='static')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
