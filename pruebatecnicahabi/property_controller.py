from typing import List, Dict

import cherrypy

from property import search_properties


class PropertyController(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_properties(self, **kwargs) -> List[Dict]:
        """
        Get method to return the information of the properties that meet the filter
        :param kwargs: filters
        :return: List with properties in json format
        """
        if cherrypy.request.method == 'GET':
            try:
                return search_properties(**kwargs)
            except Exception as e:
                raise cherrypy.HTTPError("400", str(e))
        else:
            raise cherrypy.HTTPError("404")
