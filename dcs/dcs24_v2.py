import requests
import json
import pandas as pd
import asyncio
import aiohttp

async def fetch(s, url):
    async with s.get(url) as r:
        if r.status != 200:
            return 0
        return await r.text()

async def fetch_all(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

async def import_comex_data(year=2023) -> tuple:
    """
    Importa os dados do Comexstats geral (http://comexstat.mdic.gov.br/pt/geral)
    de Importação e Exportação.

    Parametros
    -------------
    start_year: int
       Ano inicial da pesquisa.
    end_year: int
       Ano final da pesquisa.

    Retorno
    -------------
    tuple
       Tupla com dataframe exportação e dataframe importação, respectivamente.
    """
    # typeForm => 1 -> Exportação; 2 -> Importação
    estados_url = "http://api.comexstat.mdic.gov.br/pt/location/states?filter=%7B%22id%22:%22noUf%22,%22text%22:%22UF%20do%20Produto%22,%22route%22:%22/pt/location/states%22,%22type%22:%221%22,%22group%22:%22gerais%22,%22groupText%22:%22Gerais%22,%22hint%22:%22fieldsForm.general.noUf.description%22,%22placeholder%22:%22UFs%20do%20Produto%22%7D"
    lista_estados = [x["id"] for x in json.loads(requests.get(estados_url).text)]

    meses = [("01", "Janeiro"), ("02", "Fevereiro"), ("03", "Mar"), ("04", "Abril"), ("05", "Maio"), ("06", "Junho"), ("07", "Julho"), 
             ("08", "Agosto"), ("09", "Setempro"), ("10", "Outubro"), ("11", "Novembro"), ("12", "Dezembro")]
    
    exp_urls = list()
    imp_urls = list()
    
    for id_estado in lista_estados:
        for mes_num, mes in meses:
            exp_urls.append(f"http://api.comexstat.mdic.gov.br/general?filter=%7B%22yearStart%22:%22{year}%22,%22yearEnd%22:%22{year}%22,%22typeForm%22:1,%22typeOrder%22:2,%22filterList%22:%5B%7B%22id%22:%22noUf%22,%22text%22:%22UF%20do%20Produto%22,%22route%22:%22/pt/location/states%22,%22type%22:%221%22,%22group%22:%22gerais%22,%22groupText%22:%22Gerais%22,%22hint%22:%22fieldsForm.general.noUf.description%22,%22placeholder%22:%22UFs%20do%20Produto%22%7D%5D,%22filterArray%22:%5B%7B%22item%22:%5B%22{id_estado}%22%5D,%22idInput%22:%22noUf%22%7D%5D,%22rangeFilter%22:%5B%5D,%22detailDatabase%22:%5B%7B%22id%22:%22noUrf%22,%22text%22:%22URF%22%7D,%7B%22id%22:%22noUf%22,%22text%22:%22UF%20do%20Produto%22%7D,%7B%22id%22:%22noPaispt%22,%22text%22:%22Pa%C3%ADs%22%7D,%7B%22id%22:%22noBlocopt%22,%22text%22:%22Bloco%20Econ%C3%B4mico%22%7D,%7B%22id%22:%22noVia%22,%22text%22:%22Via%22%7D,%7B%22id%22:%22noNcmpt%22,%22text%22:%22NCM%20-%20Nomenclatura%20Comum%20do%20Mercosul%22,%22parentId%22:%22coNcm%22,%22parent%22:%22C%C3%B3digo%20NCM%22%7D,%7B%22id%22:%22noSh6pt%22,%22text%22:%22Subposi%C3%A7%C3%A3o%20(SH6)%22,%22parentId%22:%22coSh6%22,%22parent%22:%22Codigo%20SH6%22%7D,%7B%22id%22:%22noSh4pt%22,%22text%22:%22Posi%C3%A7%C3%A3o%20(SH4)%22,%22parentId%22:%22coSh4%22,%22parent%22:%22Codigo%20SH4%22%7D,%7B%22id%22:%22noSh2pt%22,%22text%22:%22Cap%C3%ADtulo%20(SH2)%22,%22parentId%22:%22coSh2%22,%22parent%22:%22Codigo%20SH2%22%7D,%7B%22id%22:%22noSecpt%22,%22text%22:%22Se%C3%A7%C3%A3o%22,%22parentId%22:%22coNcmSecrom%22,%22parent%22:%22Codigo%20Se%C3%A7%C3%A3o%22%7D%5D,%22monthDetail%22:true,%22metricFOB%22:true,%22metricKG%22:true,%22metricStatistic%22:true,%22monthStart%22:%22{mes_num}%22,%22monthEnd%22:%22{mes_num}%22,%22formQueue%22:%22general%22,%22langDefault%22:%22pt%22,%22monthStartName%22:%22{mes}%22,%22monthEndName%22:%22{mes}%22%7D")
            imp_urls.append(f"http://api.comexstat.mdic.gov.br/general?filter=%7B%22yearStart%22:%22{year}%22,%22yearEnd%22:%22{year}%22,%22typeForm%22:2,%22typeOrder%22:2,%22filterList%22:%5B%7B%22id%22:%22noUf%22,%22text%22:%22UF%20do%20Produto%22,%22route%22:%22/pt/location/states%22,%22type%22:%221%22,%22group%22:%22gerais%22,%22groupText%22:%22Gerais%22,%22hint%22:%22fieldsForm.general.noUf.description%22,%22placeholder%22:%22UFs%20do%20Produto%22%7D%5D,%22filterArray%22:%5B%7B%22item%22:%5B%22{id_estado}%22%5D,%22idInput%22:%22noUf%22%7D%5D,%22rangeFilter%22:%5B%5D,%22detailDatabase%22:%5B%7B%22id%22:%22noUrf%22,%22text%22:%22URF%22%7D,%7B%22id%22:%22noUf%22,%22text%22:%22UF%20do%20Produto%22%7D,%7B%22id%22:%22noPaispt%22,%22text%22:%22Pa%C3%ADs%22%7D,%7B%22id%22:%22noBlocopt%22,%22text%22:%22Bloco%20Econ%C3%B4mico%22%7D,%7B%22id%22:%22noVia%22,%22text%22:%22Via%22%7D,%7B%22id%22:%22noNcmpt%22,%22text%22:%22NCM%20-%20Nomenclatura%20Comum%20do%20Mercosul%22,%22parentId%22:%22coNcm%22,%22parent%22:%22C%C3%B3digo%20NCM%22%7D,%7B%22id%22:%22noSh6pt%22,%22text%22:%22Subposi%C3%A7%C3%A3o%20(SH6)%22,%22parentId%22:%22coSh6%22,%22parent%22:%22Codigo%20SH6%22%7D,%7B%22id%22:%22noSh4pt%22,%22text%22:%22Posi%C3%A7%C3%A3o%20(SH4)%22,%22parentId%22:%22coSh4%22,%22parent%22:%22Codigo%20SH4%22%7D,%7B%22id%22:%22noSh2pt%22,%22text%22:%22Cap%C3%ADtulo%20(SH2)%22,%22parentId%22:%22coSh2%22,%22parent%22:%22Codigo%20SH2%22%7D,%7B%22id%22:%22noSecpt%22,%22text%22:%22Se%C3%A7%C3%A3o%22,%22parentId%22:%22coNcmSecrom%22,%22parent%22:%22Codigo%20Se%C3%A7%C3%A3o%22%7D%5D,%22monthDetail%22:true,%22metricFOB%22:true,%22metricKG%22:true,%22metricStatistic%22:true,%22monthStart%22:%22{mes_num}%22,%22monthEnd%22:%22{mes_num}%22,%22formQueue%22:%22general%22,%22langDefault%22:%22pt%22,%22monthStartName%22:%22{mes}%22,%22monthEndName%22:%22{mes}%22%7D")

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=350)) as session:
        exp_dfs, imp_dfs = await fetch_all(session, exp_urls), await fetch_all(session, imp_urls)

        return (
            pd.concat([pd.DataFrame(json.loads(x)["data"]["list"]) for x in exp_dfs if x != 0], ignore_index=True),
            pd.concat([pd.DataFrame(json.loads(x)["data"]["list"]) for x in imp_dfs if x != 0], ignore_index=True),
        )

# df_exp, df_imp = asyncio.run(import_comex_data())  # --> for .py scripts
# df_exp, df_imp = await import_comex_data() # --> for .ipynb script