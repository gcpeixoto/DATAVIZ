from pandas import read_csv, Series, to_datetime
from seaborn import lineplot

def load_data(keep_orig: True, show_links: False):
    """Load data from RFB on government resource transfer."""
    
    print('Extracting data from Receita Federal do Brasil...')
    
    # extract
    df_o = read_csv('https://www.gov.br/receitafederal/dados/repasse-s.csv',sep=';')
    df = df_o.copy()

    # transform
    m, y = [], []
    for i in df['Mês / Ano de Referência'].str.split('/'):
        m.append(i[0])
        y.append('20' + i[1]) 
    df['Mês'] = m
    df['Ano'] = y
    df['Total Repassado'] = df['Total Repassado'].str.replace('.','',regex=False).apply(lambda x: float(x))
    df = df.drop('Mês / Ano de Referência',axis=1)
    
    # load
    df = df[['Mês','Ano','Entidade','Total Repassado']]
    
    print('Data loaded successfully.')
    
    if show_links:
        print(f'Extracted from: https://www.gov.br/receitafederal/dados/repasse-s.csv\n')
        print(f'Metadata on: https://www.gov.br/receitafederal/dados/repasse-s-metadados.pdf\n')
        
    if keep_orig:
        return df_o,df
    else:
        return df
    
    
def map_my(x):
    """Create simple mapping relationship between months and numbers. Like locale: pt_BR."""
    map_my = dict(zip(['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'],
                  ['0' + str(i) for i in range(1,10)] + ['10','11','12'] ))    
    
    m,y = x.split('/')
        
    return y + '-' + map_my[m]


def plot_ts_rfb(df, entity, ax, color):
    """Plot time series for specific entity."""
    
    # entity list
    elist = df['Entidade'].unique()
    
    # check
    if entity not in elist:
        
        raise ValueError(f'Possible entities are: {elist}')
    
    else:
        
        df_e = df[df['Entidade'] == entity].reset_index(drop=True)
        df_e['Período'] = Series([v['Mês'] + '/' + v['Ano'] for i,v in df_e.iterrows()])
        df_e['Período'] = to_datetime(df_e['Período'].apply(lambda x: map_my(x)))

        s1 = lineplot(data=df_e,
                        x='Período', y='Total Repassado',
                        color=color,
                        label=entity,
                        errorbar=None, 
                        ax=ax)
        
    return s1