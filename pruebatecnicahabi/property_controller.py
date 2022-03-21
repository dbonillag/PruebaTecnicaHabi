from typing import List, Dict

import cherrypy

from property import search_properties


class PropertyController(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_properties(self, **kwargs) -> List[Dict]:
        """
        Search properties
        :param kwargs:
        :return:
        """
        if cherrypy.request.method == 'GET':
            try:
                return search_properties(**kwargs)
            except Exception as e:
                raise cherrypy.HTTPError("400", str(e))
        else:
            raise cherrypy.HTTPError("404")
