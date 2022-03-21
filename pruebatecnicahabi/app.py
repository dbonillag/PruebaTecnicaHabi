import cherrypy

from pruebatecnicahabi.property_controller import PropertyController

if __name__ == '__main__':

    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': 8099}
    cherrypy.config.update(config)
    cherrypy.quickstart(PropertyController())
