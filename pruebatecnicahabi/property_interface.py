"""
class that serves as an intermediary between the api and the database
"""
from typing import List, Tuple

from connection import get_connection


def select_properties(**kwargs) -> List[Tuple]:
    vals = []
    status_filter = ""
    if kwargs.get("status"):
        vals.append(kwargs["status"])
        status_filter = "AND st.id = %s"

    year_filter = ""
    if kwargs.get("year"):
        vals.append(kwargs["year"])
        year_filter = "AND pr.year = %s"

    city_filter = ""
    if kwargs.get("city"):
        vals.append(kwargs["city"])
        city_filter = "AND pr.city = %s"
    vals_tuple = tuple(vals)

    query = f"""SELECT
        pr.*,
        st.NAME AS STATUS 
    FROM
        status_history AS sh
        INNER JOIN ( SELECT MAX( update_date ) AS update_date, property_id FROM status_history GROUP BY property_id ) AS mx_dt ON sh.property_id = mx_dt.property_id 
        AND sh.update_date = mx_dt.update_date
        INNER JOIN property AS pr ON pr.id = sh.property_id
        INNER JOIN status AS st ON st.id = sh.status_id 
    where st.id in (3,4,5)
    {status_filter}
    {year_filter}
    {city_filter}
    GROUP BY
        sh.property_id 
    ORDER BY
        sh.property_id"""

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, vals_tuple)
            result = cursor.fetchall()
    column_names = cursor.column_names
    result = [column_names, *result] if result else []
    return result
