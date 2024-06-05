from datetime import datetime, date
import pytz

# used to parse two diff types of dates '2024-05-29T19:55:25Z' or '2024-05-19  12:42:00 PM'
def parse_date(date_str):
    if isinstance(date_str, datetime):
        return date_str
    try:
         # Try to parse the date in '2024-05-19  12:42:00 PM' format
         date = datetime.strptime(date_str, "%Y-%m-%d %I:%M:%S %p")
    except ValueError:
        try:
            # Try to parse the date in '2024-05-29T19:55:25Z' format
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
            # Ensure the date is formatted with time zone
            date = date.replace(tzinfo=pytz.UTC)
        except ValueError:
            raise ValueError(f"Date format for '{date_str}' is not recognized")
    return date

def getMostRecentDate(sheet, column_id):
    submit_dates = []

    column = sheet[column_id]

    for cell in column[1:]:
        if cell.value is not None:
            submit_dates.append(cell.value)
        else:
            break

    parsed = [parse_date(date_str) for date_str in submit_dates]
    tzoned = [date.astimezone(pytz.UTC) for date in parsed]
    recent = max(tzoned).strftime("%Y-%m-%dT%H:%M:%SZ")
    print('recent', recent)

    return recent if recent else datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
    