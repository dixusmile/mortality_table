import mortality_table

tables = xlrd.open_workbook("C:/Users/wowbe/Desktop/dixusmile/2015-vbt-smoker-distinct-alb-anb.xlsx", on_demand=True)
table_new = mortality_table.data_transformation(tables)