import mortality_table
import numpy as np
import pandas as pd
import xlrd

tables = xlrd.open_workbook("C:/Users/wowbe/Desktop/dixusmile/2015-vbt-smoker-distinct-alb-anb.xlsx", on_demand=True)
table_new = mortality_table.data_transformation(tables)