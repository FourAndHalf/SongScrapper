from django.db import connection

def fetch_artists():
    """
    Fetches all artists from the JIM_CODES table.
    """

    with connection.cursor() as cursor:
        cursor.execute("SELECT JCODE_CODE, JCODE_DESC FROM JIM_CODES WHERE JCODE_TYPE = 'ARTIST'")
        rows = cursor.fetchall()
    return rows

def fetch_genres():
    """
    Fetches all genres from the JIM_CODES table.
    """

    with connection.cursor() as cursor:
        cursor.execute("SELECT JCODE_CODE, JCODE_DESC FROM JIM_CODES WHERE JCODE_TYPE = 'GENRE'")
        rows = cursor.fetchall()
    return rows