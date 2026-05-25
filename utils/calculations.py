from datetime import date

def calculate_cutoff_date(years_ago):

    today = date.today()

    try:
        cutoff_date = today.replace(
            year=today.year - years_ago
        )

    except ValueError:
        cutoff_date = today.replace(
            year=today.year - years_ago,
            day=today.day - 1
        )

    return cutoff_date