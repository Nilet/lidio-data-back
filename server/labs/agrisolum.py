from datetime import datetime
import pytz


def agrisolum2inceres(df):
    for column in df.columns:
        print(column)

    df = df.rename(columns={'Descrição da Amostra': 'id', 'Profundidade': 'prof', 'Al3+': 'Al', 'Areia Fina': 'Areia fina',
                            'Areia Grossa': 'Areia grossa', 'Areia Total': 'Areia total', 'Argila': 'Argila', 'B': 'B',
                            'Carbono (C)': 'C', 'Ca2+': 'Ca', 'CTC pH 7,0': 'CTC', 'Cu2+': 'Cu', 'Fe2+': 'Fe',
                            'Mg2+': 'Mg', 'Mn2+': 'Mn', 'Na+': 'Na', 'pH (H2O)': 'pH Agua',
                            'pH CaCl2': 'pH CaCl2', 'pH SMP': 'ph_smp', 'P meh': 'P mehl', 'P rem': 'prem', 'P res': 'P res',
                            'Ca/K': 'Ca/K', 'Ca/Mg': 'Ca/Mg', 'K/Ca+Mg': 'Ca+Mg/K', 'Mg/K': 'Mg/K', 'S': 'S', 'm': 'Al%',
                            'Ca': 'Ca%', 'H': 'H%', 'K': 'K%', 'Mg': 'Mg%', 'SB': 'SB', 'Silte': 'Silte', 'CTC Efetiva': 't',
                            'Zn2+': 'Zn', 'Matéria Orgânica (MO)': 'MOS','Matéria Orgãnica (MO)': 'MOS', 'V': 'V%', 'v': 'V%',
                            'K+': 'K', 'K2+': 'K'
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
    try:
        df['m%'] = (df['Al'].astype(float) * 100) / df['t'].astype(float)
    except:
        df['m%'] = 'ns'
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


def agrisolum2datafarm(df):
    df = df.rename(columns={'nº Laborat.': 'Codigo Amostra', 'Proprietário': 'Produtor', 'Propriedade': 'Fazenda',
                            'Lote / Talhão': 'Talhão', 'Descrição da Amostra': 'Nro do Ponto', 'pH CaCl2': 'pH (CaCl2)',
                            'H+ + Al3+': 'Hidrogênio + Alumínio', 'Al3+': 'Alumínio', 'Ca2+': 'Cálcio', 'Mg2+': 'Magnésio',
                            'K2+': 'Potássio (Resina)', 'SB': 'Soma de bases', 'CTC pH 7,0': 'Capac. de troca de cátions',
                            'Matéria Orgãnica (MO)': 'Matéria Orgânica', 'P meh': 'Fósforo (Mehlich)', 'S': 'Enxofre',
                            'B': 'Boro', 'Cu2+': 'Cobre', 'Fe2+': 'Ferro', 'Mn2+': 'Manganês', 'Zn2+': 'Zinco',
                            'Ca': '% de Cálcio na CTC', 'Mg': '% de Magnésio na CTC', 'K': '% de Potássio na CTC',
                            'm': 'Saturação por Al', 'H': '% de H°+Al ³  na C.T.C.', 'v': 'Saturação por bases',
                            'Mg/K': 'Relação Mg/K', 'Argila': 'Argila', 'Silte': 'Silte', 'Areia Total': 'Areia Total'
                            })

    df['Data'] = datetime.now().astimezone(
        pytz.timezone('Etc/GMT-3')).strftime('%d/%m/%Y')
    df = df.loc[:, ['Data', 'Codigo Amostra', 'Produtor', 'Fazenda', 'Talhão', 'Nro do Ponto',
                    'Profundidade', 'pH (H2O)', 'pH (CaCl2)', 'Hidrogênio + Alumínio', 'Alumínio',
                    'Cálcio', 'Magnésio', 'Potássio (Resina)', 'Soma de bases',
                    'Capac. de troca de cátions', 'Matéria Orgânica', 'Fósforo (Mehlich)', 'Enxofre',
                    'Boro', 'Cobre', 'Ferro', 'Manganês', 'Zinco', '% de Cálcio na CTC', '% de Magnésio na CTC',
                    '% de Potássio na CTC', 'Saturação por Al', '% de H°+Al ³  na C.T.C.', 'Saturação por bases',
                    'Relação Mg/K', 'Argila', 'Silte', 'Areia Total']]

    df = insert_row(0, df, ['', '', '', '', '', '', '', '-', '-', 'cmolc/dm3', 'cmolc/dm3', 'cmolc/dm3', 'cmolc/dm3',
                            'cmolc/dm3', 'cmolc/dm3', 'cmolc/dm3', '%', 'mg/dm3', 'mg/dm3', 'mg/dm3', 'mg/dm3',
                            'mg/dm3', 'mg/dm3', 'mg/dm3', '%', '%', '%', '%', '%', '%', '-', '%', '%', '%'])

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
