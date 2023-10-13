import openpyxl

template = './driver_template.xltx'

# {'Driver Designation': 'Pro - Am', 'Team Name': 'RealTime', 'number': '43', 'event': 'Road America', 'series': 'GTWCA', 'driver2': 'Adam Christodoulou', 'driver1': 'Anthony Bartone'}

header_mapping = {
    'number': 'Car #',
    'Team Name': 'Team',
    'driver1': 'Driver 1',
    'driver2': 'Driver 2',
    'Signature': 'Signature',
    'Signature2': 'Signature2'
}

# data ==  array or dict


def fill_excel_template(data, template_path, output_path):
    wb = openpyxl.load_workbook(template)
    sheet = wb.active

    for row_i, row_data in enumerate(data, start=2):
        for col_i, key in enumerate(row_data.keys(), start=1):

            if key in header_mapping:

                mapped_header = header_mapping[key]
                # Get the column index for the mapped header
                col_i = sheet[1].index(mapped_header) + 1
                sheet.cell(row=row_i, column=col_i).value = row_data[key]
    wb.save()