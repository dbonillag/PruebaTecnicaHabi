"""
Class Property
"""
import json
from typing import List, Dict, Tuple

from property_interface import select_properties


def search_properties(**kwargs) -> List[Dict]:
    properties = select_properties(**kwargs)
    if properties:
        properties_list = map_properties(properties)
        #properties_list = json.dumps(properties_list, indent=4)
        return properties_list
    return []


def map_properties(properties: List[Tuple]) -> List[Dict]:
    column_names = properties[0]

    structured_properties = list(map(lambda p:
                                     {
                                         column_names[i]: data for i, data in enumerate(p)
                                     }, properties[1:]))

    return structured_properties
