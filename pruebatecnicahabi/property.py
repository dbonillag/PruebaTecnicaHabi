"""
Class Property
"""
import json
from typing import List, Dict, Tuple

from property_interface import select_properties


def search_properties(**kwargs) -> List[Dict]:
    """
    Search for the properties according to the filters and return them in a format according to what is expected by the endpoint
    :param kwargs: filters
    :return: list with found properties
    """
    properties = select_properties(**kwargs)
    if properties:
        properties_list = map_properties(properties)
        return properties_list
    return []


def map_properties(properties: List[Tuple]) -> List[Dict]:
    """
    Map property information
    :param properties: properties in tuple format
    :return: properties in dictionary format
    """
    column_names = properties[0]

    structured_properties = list(map(lambda p:
                                     {
                                         column_names[i]: data for i, data in enumerate(p)
                                     }, properties[1:]))

    return structured_properties
