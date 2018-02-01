import pandas as pd

def deltaize(file1, file2, check_fields, indicator=True, how='outer'):
    for input in [file1,file2,how]:
        if type(input) != str:
            raise ValueError("The inputs for file1, file2, and how must be a string\nexiting...")
    if type(indicator) != bool:
        raise ValueError("The indicator value must be a boolean\nexiting...")
    if type(check_fields) not in [list, str]:
        raise ValueError("Check_fields must be a list, or a string\nexiting...")

    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    dfmerge = pd.merge(df1, df2, on=check_fields, indicator=indicator, how=how)

    return dfmerge

def delta_to_excel(file1, file2, check_fields, broken_out='yes', workbook_name='', indicator=True, how='outer'):
    dfmerge = deltaize(file1, file2, check_fields, indicator, how)

    for input in [broken_out,workbook_name,how]:
        if input != str:
            raise ValueError("The inputs for broken_out and workbook_name must be a string\nexiting...")

    sheets=[]

    if broken_out == 'yes':
        inBoth = dfmerge.query("_merge == 'both'")
        leftOnly = dfmerge.query("_merge == 'left_only'")
        rightOnly = dfmerge.query("_merge == 'right_only'")

        sheets.extend((inBoth, leftOnly, rightOnly))
        print sheets


    writer = pd.ExcelWriter('Output_Delta.xlsx')

    dfmerge.to_excel(writer, "Full Merge")
    if len(sheets) > 0:
        inBoth.to_excel(writer, "inBoth")
        leftOnly.to_excel(writer, "leftOnly")
        rightOnly.to_excel(writer, "rightOnly")

    writer.save()



# dfm = deltaize('CHCP_eCWApptBlocks_20180131080521.xlsx','CHCP_eCWApptBlocks_20180131200521.xlsx', ['db_name','UserId','PrintName','StartDate','EndDate','StartTime','EndTime','AllDay','Description','facilityId'])

# delta_to_excel('CHCP_eCWApptBlocks_20180131080521.xlsx','CHCP_eCWApptBlocks_20180131200521.xlsx', ['db_name','UserId','PrintName','StartDate','EndDate','StartTime','EndTime','AllDay','Description','facilityId'], broken_out='no')