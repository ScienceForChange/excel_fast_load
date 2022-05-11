# excel_fast_load
Load XLSX/XLSM files into pandas dataframes faster than pandas.read_excel

author: [FelixKling](https://felix-kling.de/)

NOTE: Science for Change just packages this code to use it because we find it useful for Citizen Science projects!

This code is provided as is, with no license and no warranties, as it was shared by Felix:
https://stackoverflow.com/a/62277641

## Usage
```
from excel_fast_load import excel_fast_load
dataframe = excel_fast_load('path/to/excelfile.xlsx')
```
### Optional parameters after path

`sheet_name`: str. Name of the sheet to read. If none, the first (not the active!) sheet is read. The default is None.

`header`: bool. Whether to use the first line as column headers. The default is True.

`index_col`: bool. Whether to use the first column as index. The default is False.

`skiprows`: list of int. The row numbers to skip ([0, 1] skips the first two rows). The default is []. 

`skipcolumns`: list of int. The column numbers to skip ([0, 1] skips the first two columns). The default is [].

### Raises

`TypeError` If the file is no .xlsx or .xlsm file.
`FileNotFoundError` If the sheet name is not found.

### Returns
`Pandas.DataFrame`. The input file as DataFrame.

