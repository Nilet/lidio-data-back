def agrisolum_formatter(df):
    print(df.columns)
    df = df.rename(columns={'Descrição da Amostra': 'id', 'Profundidade': 'prof', 'Al3+': 'Al', 'Areia Fina': 'Areia fina',
                            'Areia Grossa': 'Areia grossa', 'Areia Total': 'Areia total', 'Argila': 'Argila', 'B': 'B',
                            'Carbono (C)': 'C', 'Ca2+': 'Ca', 'CTC pH 7,0': 'CTC', 'Cu2+': 'Cu', 'Fe2+': 'Fe', 'K2+': 'K',
                            'Mg2+': 'Mg', 'Mn2+': 'Mn', 'Matéria Orgãnica (MO)': 'MOS', 'Na+': 'Na', 'pH (H2O)': 'pH Agua',
                            'pH CaCl2': 'pH CaCl2', 'pH SMP': 'ph_smp', 'P meh': 'P mehl', 'P rem': 'prem', 'P res': 'P res',
                            'Ca/K': 'Ca/K', 'Ca/Mg': 'Ca/Mg', 'K/Ca+Mg': 'Ca+Mg/K', 'Mg/K': 'Mg/K', 'S': 'S', 'm': 'Al%',
                            'Ca': 'Ca%', 'H': 'H%', 'K': 'K%', 'Mg': 'Mg%', 'SB': 'SB', 'Silte': 'Silte', 'CTC Efetiva': 't',
                            'v': 'V%', 'Zn2+': 'Zn'
                            })

    df['AlS'] = ''
    df['Altimetria SRTM'] = ''
    df['Ca+Mg'] = ''
    df['CaS'] = ''
    df['CEa'] = ''
    df['Cl'] = ''
    df['CO3'] = ''
    df['Ds'] = ''
    df['Fe/Mn'] = ''
    df['FeO'] = ''
    df['H'] = ''
    df['H/Al'] = ''
    df['HCO3'] = ''
    df['K mg'] = ''
    df['K/Na'] = ''
    df['KS'] = ''
    df['m%'] = ''
    df['MgS'] = ''
    df['N'] = ''
    df['NaS'] = ''
    df['NH4'] = ''
    df['NO3'] = ''
    df['P'] = ''
    df['PB'] = ''
    df['pH'] = ''
    df['ph_kcl'] = ''
    df['PO'] = ''
    df['P_Total'] = ''
    df['P/Zn'] = ''
    df['RAS'] = ''
    df['H/Al%'] = ''
    df['Na%'] = ''
    df['Si'] = ''
    df['SO4'] = ''
    df['S/P'] = ''

    df = df.loc[:, ['id', 'prof', 'Al', 'AlS', 'Altimetria SRTM', 'Areia fina', 'Areia grossa',
                    'Areia total', 'Argila', 'B', 'C', 'Ca', 'Ca+Mg', 'CaS', 'CEa', 'Cl', 'CO3',
                    'CTC', 'Cu', 'Ds', 'Fe', 'Fe/Mn', 'FeO', 'H', 'H/Al', 'HCO3', 'K', 'K mg', 'K/Na',
                    'KS', 'm%', 'Mg', 'MgS', 'Mn', 'MOS', 'N', 'Na', 'NaS', 'NH4', 'NO3', 'P', 'PB', 'pH',
                    'pH Agua', 'pH CaCl2', 'ph_kcl', 'ph_smp', 'P mehl', 'PO', 'prem', 'P res', 'P_Total',
                    'P/Zn', 'RAS', 'Ca/K', 'Ca/Mg', 'Ca+Mg/K', 'Mg/K', 'S', 'Al%', 'Ca%', 'H%', 'H/Al%',
                    'K%', 'Mg%', 'Na%', 'SB', 'Si', 'Silte', 'SO4', 'S/P', 't', 'V%', 'Zn']]

    df['id'] = df['id'].str.replace('PONTO ', '')
    df['prof'] = df['prof'].str.replace(' CM', '')
    df = insert_row(0, df, ['', '', 'cmolc/dm³', 'meq/L', 'metros', '%',
                            '%', '%', '%', 'ppm', 'cmolc/dm³', 'cmolc/dm³', 'cmolc/dm³',
                                           'meq/L', 'dS/m', 'ppm', 'meq/L', 'cmolc/dm³', 'ppm', 'g/dm³',
                                           'ppm', 'Sem Unidade', '%', 'cmolc/dm³', 'cmolc/dm³', 'meq/L',
                                           'cmolc/dm³', 'ppm', 'Sem Unidade', 'meq/L', '%',	'cmolc/dm³',
                                           'meq/L',	'ppm', '%',	'cmolc/dm³', 'cmolc/dm³', 'meq/L',
                                           'meq/L',	'meq/L', 'ppm', 'ppm', 'Sem Unidade', 'Sem Unidade',
                                           'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'ppm', 'ppm', 'ppm', 'ppm', 'ppm', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade',
                                           'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'ppm', '%', '%',
                                           '%', '%', '%', '%', '%', 'cmolc/dm³', '%', '%', 'meq/L', 'Sem Unidade',
                                           'cmolc/dm³', '%', 'ppm'])
    return df


def insert_row(row_number, df, row_value):
    start_upper = 0

    end_upper = row_number

    start_lower = row_number

    end_lower = df.shape[0]

    upper_half = [*range(start_upper, end_upper, 1)]

    lower_half = [*range(start_lower, end_lower, 1)]

    lower_half = [x.__add__(1) for x in lower_half]

    index_ = upper_half + lower_half

    df.index = index_

    df.loc[row_number] = row_value

    df = df.sort_index()

    df = df.drop(1)

    return df
