class DataReader:

    def readDataForLogin():
        book = xlrd.open_workbook('data.xlsx')
        first_sheet = book.sheet_by_index(0)
        uname,pwd = tuple(first_sheet.row_slice(rowx=1, start_colx=0))
        uname = str(uname).split(':')
        uname = str(uname[1][:-2])
        pwd = str (pwd)
        pwd = pwd[7:-1]
        return uname,pwd

if __name__=="__main__":
    DataReader.readDataForLogin()