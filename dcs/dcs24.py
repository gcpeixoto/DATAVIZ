from pandas import read_csv
import io, os, requests
from warnings import filterwarnings

# remove warning launched by requests
filterwarnings("ignore")

def load_files(year: int,path: str):
    """Simple function to load import/export files"""

    imp = read_csv(os.path.join(path,'imports.csv'))
    exp = read_csv(os.path.join(path,'exports.csv'))
    cc = read_csv(os.path.join(path,'country-codes.csv'))
    
    print(f'COMEX files successfuly loaded from: {path}')
    
    return imp, exp, cc

def get_comex(year: int):
    """Try to load pre-stored foreign trade (COMEXStats) files. Otherwise, pull from MDIC.GOV.BR"""

    target_dir = '../data/comex-' + str(year)

    try:

        # pre-stored files
        imp, exp, cc = load_files(year,target_dir)

    except:
        
        print(f'COMEX files unavailable for year {year}. Trying to download from GOV.BR...')

        # URLs
        root = 'https://balanca.economia.gov.br/balanca/bd/'
        imp = 'comexstat-bd/ncm/' + 'IMP_' + str(year) + '.csv' # imports
        exp = 'comexstat-bd/ncm/' + 'EXP_' + str(year) + '.csv' # exports
        bc = 'tabelas/PAIS_BLOCO.csv' # block codes
        cc = 'tabelas/PAIS.csv' # country codes

        # SSL verification not necessary for this class example
        trade = lambda x: read_csv(io.StringIO(requests.get(root + x,verify=False).content.decode('utf-8')),sep=';')
        imp, exp = trade(imp), trade(exp)

        # country/block codes
        bc = read_csv(io.StringIO(requests.get(root + bc,verify=False).content.decode('ISO-8859-1')), sep =';', usecols = [0,2])
        cc = read_csv(io.StringIO(requests.get(root + cc,verify=False).content.decode('ISO-8859-1')), sep =';', usecols = [0,3])
        cc = cc.merge(bc, on = 'CO_PAIS')

        # rename
        imp = imp.rename(columns=dict(zip(imp.keys(),
        ['Ano','Mês','NCM','Unidade estatística','País de origem','UF de destino',
        'Meio de transporte','URF desembarque','Quantidade estatística','Kg líquido',
        'Valor Free On Board','Valor de frete','Valor de seguro'])))

        exp = exp.rename(columns=dict(zip(exp.keys(),
        ['Ano','Mês','NCM','Unidade estatística','País de destino','UF de origem',
        'Meio de transporte','URF embarque','Quantidade estatística','Kg líquido',
        'Valor Free On Board','Valor de frete','Valor de seguro'])))

        cc = cc.rename(columns=dict(zip(cc.keys(),['Código do país','Nome do país','Nome do bloco'])))
        #cc = dict(zip(cc['Código do país'],cc['Nome do país']))

        # save to dir
        os.makedirs(target_dir,exist_ok=False)
        imp.to_csv(os.path.join(target_dir,'imports.csv'),index=False)
        exp.to_csv(os.path.join(target_dir,'exports.csv'),index=False)
        cc.to_csv(os.path.join(target_dir,'country-codes.csv'),index=False)

        # load saved files
        imp, exp, cc = load_files(year,target_dir)
        
    finally:
        
        return imp, exp, cc, target_dir