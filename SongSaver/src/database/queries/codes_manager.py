from django.db import connection

def fetch_code_by_type(type):
    """
    Fetches all data from the JIM_CODES table with a particular type.
    """
    with connection.cursor() as cursor:
        cursor.execute('SELECT "JCODE_CODE", "JCODE_DESC" FROM "JIM_CODES" WHERE "JCODE_TYPE" = %s', [type])
        rows = cursor.fetchall()
    return [(row[0], row[1]) for row in rows]


def fetch_value_by_type_and_code(type, code):
    """
    Fetches value from the JIM_CODES table with a particular type and code.
    """
    with connection.cursor() as cursor:
        cursor.execute('SELECT "JCODE_CODE", "JCODE_DESC" FROM "JIM_CODES" WHERE "JCODE_TYPE" = %s', [type])
        rows = cursor.fetchall()
    return rows