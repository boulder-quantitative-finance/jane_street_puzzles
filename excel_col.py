# def excel_col(i):
# 	d = (i-1) / 26
# 	m = (i-1) % 26
# 	if i != 0:
# 		return excel_col(d) + chr(m+ord('A'))
# 	else:
# 		return ""

def excel_col(col):
    """Covert 1-relative column number to excel-style column label."""
    quot, rem = divmod(col-1,26)
    return excel_col(quot) + chr(rem+ord('A')) if col!=0 else ''

print(excel_col(4))
