from openpyxl import Workbook

def write_data_to_excel(data, output_path):
    workbook = Workbook()
    sheet = workbook.active

    for row in data:
        sheet.append(row)

    workbook.save(output_path)