import openpyxl

def UpdateExcelData(FilePath,FruitName,ColName,NewValue):
    book = openpyxl.load_workbook(FilePath)
    Sheet = book.active
    cell = {}
    for i in range(1,Sheet.max_column+1):
        if Sheet.cell(1,i).value == ColName:
            cell["col"] = i

    for i in range(1,Sheet.max_row+1):
        for j in range(1,Sheet.max_column+1):
            if Sheet.cell(i,j) == FruitName:
                cell["row"] = i
    Sheet.cell(cell["row"],cell["col"]).value = NewValue
    book.save(FilePath)


