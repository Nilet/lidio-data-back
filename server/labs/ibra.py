def ibra2inceres(df):
    df = df.drop(0)
    df = df.drop(1)

    df['id'] = df['Identificação'].str.split(' | ').str[0]
    
    df['prof'] = df['Identificação'].str.split('Prof.: ').str[1]
    df['prof'] = df['prof'].apply(fix_prof)
    
    df.rename(columns={'Prof': 'Prof'}, inplace=True)
    df = df.rename(columns={'Alumínio Trocável': 'Al', 'Areia Total': 'Areia total', 'Argila': 'Argila', 'Boro (Água Quente)': 'B',
                            'Carbono Orgânico Total': 'C', 'Cálcio (Resina)': 'Ca', 'Capac. de troca de cátions': 'CTC', 
                            'Cobre (DTPA)': 'Cu', 'Ferro (DTPA)': 'Fe', 'Hidrogênio': 'H', 'Acidez Total': 'H/Al',
                            'Potássio (Resina)': 'K', 'Magnésio (Resina)': 'Mg', 'Manganês (DTPA)': 'Mn', 
                            'Matéria Orgânica (NIR - Oxidação)': 'MOS', 'Nitrogênio Total - NIR':'N', 'Sódio (Mehlich)': 'Na',
                            'pH (CaCl2)': 'pH CaCl2', 'pH (SMP)': 'ph_smp', 'Fósforo (Mehlich)': 'P mehl', 'Fósforo (Resina)': 'P res',
                            'Relação Ca/K': 'Ca/K', 'Relação Ca/Mg': 'Ca/Mg', 'Relação Mg/K': 'Mg/K', 'Enxofre (Fosfato de Cálcio)':'S',
                            '% de Alumínio na CTC': 'Al%', '% de Cálcio na CTC': 'Ca%', '% de Hidrogênio na CTC': 'H%',
                            '% de Potássio na CTC': 'K%', '% de Magnésio na CTC': 'Mg%', '% de Sódio na C.T.C.': 'Na%', 'Soma de bases': 'SB',
                            'Silte': 'Silte', 'Saturação por bases': 'V%', 'Zinco (DTPA)': 'Zn'
                            })
    
    df['MOS'] = df['MOS'].astype(float) / 10
    df['C'] = df['C'].str.replace(",", ".").astype(float).apply(convert_g_to_cmol) / 120
    df['Ca'] = df['Ca'].astype(float) / 10
    df['CTC'] = df['CTC'].str.replace(",", ".").astype(float) / 10
    df['H'] = df['H'].str.replace(",", ".").astype(float) / 10
    df['H/Al'] = df['H/Al'].str.replace(",", ".").astype(float) / 10
    df['K'] = df['K'].str.replace(",", ".").astype(float) / 10
    df['Mg'] = df['Mg'].str.replace(",", ".").astype(float) / 10
    df['N'] = df['N'].str.replace(",", ".").astype(float).apply(convert_percent_to_cmol) / 140
    df['Na'] = df['Na'].str.replace(",", ".").astype(float) / 10
    df['SB'] = df['SB'].str.replace(",", ".").astype(float) / 10
    df['Silte'] = df['Silte'].str.replace(",", ".").astype(float) / 10
    df['Areia total'] = df['Areia total'].str.replace(",", ".").astype(float) / 10
    df['Argila'] = df['Argila'].str.replace(",", ".").astype(float) / 10
    df['t']= df['Ca'] + df['Mg']+ df['K'] + df['Al'].str.replace(",",".").astype(float)
    
    df['AlS'] =''
    df['Areia fina'] = ''
    df['Areia grossa'] = ''
    df['Ca+Mg'] = ''
    df['CaS'] = ''
    df['CEa'] = ''
    df['Cl'] = ''
    df['CO3'] = ''
    df['Ds'] =''
    df['Fe/Mn'] = ''
    df['FeO'] = ''
    df['HCO3'] = ''
    df['K mg'] = ''
    df['K/Na'] = ''
    df['KS'] = ''
    df['m%'] = ''
    df['MgS'] = ''
    df['NaS'] = ''
    df['NH4'] = ''
    df['NO3'] = ''
    df['P'] = ''
    df['PB'] = ''
    df['pH'] = ''
    df['pH Agua'] = ''
    df['ph_kcl'] = ''
    df['PO'] = ''
    df['prem'] = ''
    df['P_Total'] =''
    df['P/Zn'] = ''
    df['RAS'] = ''
    df['Ca+Mg/K'] = ''
    df['H/Al%'] = ''
    df['Si'] = ''
    df['SO4'] = ''
    df['S/P'] = ''
    
    df = df.loc[:, ['id', 'prof', 'Al', 'AlS', 'Areia fina', 'Areia grossa',
                    'Areia total', 'Argila', 'B', 'C', 'Ca', 'Ca+Mg', 'CaS', 'CEa', 'Cl', 'CO3',
                    'CTC', 'Cu', 'Ds', 'Fe', 'Fe/Mn', 'FeO', 'H', 'H/Al', 'HCO3', 'K', 'K mg', 'K/Na',
                    'KS', 'm%', 'Mg', 'MgS', 'Mn', 'MOS', 'N', 'Na', 'NaS', 'NH4', 'NO3', 'P', 'PB', 'pH',
                    'pH Agua', 'pH CaCl2', 'ph_kcl', 'ph_smp', 'P mehl', 'PO', 'prem', 'P res', 'P_Total',
                    'P/Zn', 'RAS', 'Ca/K', 'Ca/Mg', 'Ca+Mg/K', 'Mg/K', 'S', 'Al%', 'Ca%', 'H%', 'H/Al%',
                    'K%', 'Mg%', 'Na%', 'SB', 'Si', 'Silte', 'SO4', 'S/P', 't', 'V%', 'Zn']]
    
    df = insert_row(0, df, ['', '', 'cmolc/dm³','meq/L', '%', '%', '%', '%', 'ppm', 'cmolc/dm³','cmolc/dm³', 'cmolc/dm³',
                            'meq/L', 'dS/m', 'ppm', 'meq/L', 'cmolc/dm³', 'ppm', 'g/dm³', 'ppm', 'Sem Unidade', '%',
                            'cmolc/dm³', 'cmolc/dm³', 'meq/L', 'cmolc/dm³', 'ppm', 'Sem Unidade', 'meq/L', '%', 'cmolc/dm³',
                            'meq/L', 'ppm', '%', 'cmolc/dm³', 'cmolc/dm³', 'meq/L', 'meq/L', 'meq/L', 'ppm', 'ppm',
                            'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'ppm', 'ppm', 'ppm', 'ppm', 'ppm',
                            'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'Sem Unidade', 'ppm', 
                            '%','%','%','%','%','%','%', 'cmolc/dm³', '%', '%', 'meq/L', 'Sem Unidade', 'cmolc/dm³', '%', 'ppm'])
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

    # df = df.drop(1)

    return df

def convert_g_to_cmol(g_per_dm3):
    cmol_per_dm3 = g_per_dm3 * 1000
    return cmol_per_dm3

def convert_percent_to_cmol(percent):
    cmol_per_percent = percent * 10
    return convert_g_to_cmol(cmol_per_percent)

def fix_prof(value):
    if value == "20 a 40 cm":
        return "20-40"
    elif value == "0 a 20 cm":
        return "0-20"
    else:
        return value
