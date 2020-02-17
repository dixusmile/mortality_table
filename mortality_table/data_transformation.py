import pandas
import numpy

def data_transformation(tables):
    names = tables.sheet_names()
    tables_new = pandas.DataFrame()
    for i in range(len(names)):
        table = pandas.read_excel(tables, sheet_name=i, skiprows=2)
        name = names[i]
        age_basis = name[9:12]
        if name[5:6] == "M":
            gender = "Male"
        else:
            gender = "Female"
        if name[6:8] == "SM":
            tobacco_status = "Tobacco"
        else:
            tobacco_status = "Nontobacco"
        table_new_all = pandas.DataFrame()
        for j in range(table['Iss. Age'].min(), table['Iss. Age'].max() + 1):
            insure_age = j
            duration = pandas.DataFrame({'duration': range(1, 120 + 2 - insure_age)})
            mortality_rate = numpy.concatenate((table.loc[table['Iss. Age'] == insure_age].iloc[:, 1:26].T.values,
                                             table.loc[table['Iss. Age'] >= insure_age, ["Ult."]].values))
            mortality_rate = pandas.DataFrame({'mortality_rate': mortality_rate[:, 0]})
            table_new = pandas.concat([duration, mortality_rate], axis=1)
            table_new['insure_age'] = insure_age
            table_new['tobacco_status'] = tobacco_status
            table_new['gender'] = gender
            table_new['age_basis'] = age_basis
            table_new = table_new[['age_basis', 'gender', 'tobacco_status', 'insure_age', 'duration', 'mortality_rate']]
            table_new_all = table_new_all.append(table_new, ignore_index=True)
        tables_new = tables_new.append(table_new_all, ignore_index=True)
    return tables_new