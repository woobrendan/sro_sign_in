from datetime import datetime, date
import pytz

# used to parse two diff types of dates '2024-05-29T19:55:25Z' or '2024-05-19  12:42:00 PM'
def parse_date(date_str):
    if isinstance(date_str, datetime):
        if date_str.tzinfo is None:
            date_str = date_str.replace(tzinfo=pytz.UTC)
        return date_str
    try:
        # Try to parse the date in '2024-05-19 12:43' format
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        date = date.replace(tzinfo=pytz.UTC)
    except ValueError:
        try:
            # Try to parse the date in '2024-05-19T12:57:00Z' format
            date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
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

    # Find the most recent datetime
    recent = max(parsed, default=None)

    if recent is not None:
        recent = recent.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        recent = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return recent
    