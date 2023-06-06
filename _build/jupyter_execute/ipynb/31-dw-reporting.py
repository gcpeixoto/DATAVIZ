#!/usr/bin/env python
# coding: utf-8

# (cap:reporting-html)=
# 
# # _Dataviz Workshop_: _Data Reporting_ com HTML/PDF

# ## Objetivos do workshop
# 
# - Apresentar o módulo `xhtml2pdf` para conversão de código HTML para PDF;
# - Converter DataFrame para código HTML;
# - Desenvolver _workflow_ básico para geração de relatórios automatizados utilizando templates HTML atualizáveis utilizando dados sobre crimes violentos letais intencionais em João Pessoa.

# ## Ferramentas utilizadas
# 
# - Módulos Python    
#     - `xhtml2pdf`
#     - `re`
#     - `pandas`

# ## _Data reporting_
# 
# Existem diversas ferramentas para operacionalizar PDFs, seja para análise (_parsing_), extração, encriptação ou conversão de informações. Algumas delas, com suporte em Python são: 
# 
# - pdfminer.six
# - pyPDF2
# - reportlab
# - json2pdf
# - pymupdf
# - pikepdf
# 
# Entretanto a arte do _data reporting_, que consiste em gerar relatórios automatizados a partir de dados e exportá-los, principalmente em arquivos PDF ma forma de brochuras, portfólios, ou _one-pagers_, depende da um misto de habilidades e, às vezes, da integração de mais de uma API.
# 
# Cada uma das bibliotecas acima possuem forças e fraquezas, de maneira que, raramente, teremos à mão, soluções imediatas para gerarmos nossos relatórios.
# 
# A proposta deste capítulo é apresentar os módulos `xhtml2pdf` e `reportlab` como primeiras aproximações ao tema.

# ### `xhtml2pdf`
# 
# O módulo `xhtml2pdf` oferece uma maneira ágil de automatizar a geração de PDFs a partir de conteúdo HTML.  Ele utiliza a a biblioteca `reportlab` como _backbone_.
# 
# Ele funciona com base em _templates_ mínimos de layouts inspirados em estilos CSS. As partes principais são os objetos `@page` e `@frame`, os quais emolduram o conteúdo em página. Além disso, são disponíveis _tags_ do tipo PDF-vendor, que habilitam o desenvolvedor a inserir informações nativas de arquivos PDF, tais como paginação, sumário e idioma.
# 
# Em termos de gráficos, o módulo fornece algumas representações visuais, tais como gráficos de linhas e de barras, mas é bastante limitado.
# 
# Algumas suas vantagens são: 
# 
# - flexibilidade para gerar múltiplos _templates_ de página;
# - encriptação e assinatura;
# - superposição de marca d'água;

# ### Instalação
# 
# Recomenda-se utilizar _pip_ com: `pip install xhtml2pdf`.

# In[1]:


from xhtml2pdf import pisa
import pandas as pd, re


# ## _Workflow_ demonstrativo

# - Primeiramente, geramos um conteúdo básico em HTML que, na prática, seria a composição de um _briefing_ atualizável periodicamente e dados obtidos de um DataFrame.

# In[2]:


# geração de HTML atualizável
def html_data(table):
    text = f'\
        <h2>Dados</h2>\
        <p>Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Ultricies mi eget mauris pharetra et ultrices neque ornare aenean.\
        Sit amet cursus sit amet. Varius vel pharetra vel turpis nunc eget lorem. Enim lobortis scelerisque fermentum dui faucibus.\
        Nibh tellus molestie nunc non blandit massa enim nec dui. Non nisi est sit amet facilisis magna.\
        {table.to_html(index=False)}\
        </p>\
        <h2>Análise</h2>\
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
        Viverra ipsum nunc aliquet bibendum enim facilisis. Dui nunc mattis enim ut tellus elementum sagittis vitae. Sed adipiscing diam donec adipiscing tristique.\
        Ut sem nulla pharetra diam sit. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet.\
        Elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Pharetra convallis posuere morbi leo. Et magnis dis parturient montes nascetur.\
        Tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed. Amet justo donec enim diam vulputate ut pharetra sit amet. Tempor nec feugiat nisl pretium fusce id velit.\
        Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan. Mollis nunc sed id semper risus in hendrerit gravida rutrum. Ultrices vitae auctor eu augue ut.\
        Sit amet nisl suscipit adipiscing bibendum est ultricies integer. Urna condimentum mattis pellentesque id. Quisque non tellus orci ac auctor augue.\
        Dolor sed viverra ipsum nunc aliquet bibendum enim.\
        \n\
        Et malesuada fames ac turpis egestas. Pretium nibh ipsum consequat nisl vel pretium. Consectetur adipiscing elit ut aliquam purus.\
        Duis at consectetur lorem donec massa. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. In iaculis nunc sed augue lacus viverra.\
        Malesuada fames ac turpis egestas maecenas pharetra convallis. Massa sed elementum tempus egestas. Turpis egestas maecenas pharetra convallis posuere morbi. \
        Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus. Tempus iaculis urna id volutpat.\
        \n'
    
    return text


# - Em seguida fazemos o carregamento dos dados que serão usados para compor o relatório. Na prática, poderia já ser um gráfico pós-processado.

# In[3]:


df = pd.read_csv('../data/crimes-pb-2015-2018.csv')


# - Fazemos o carregamento de um _template_ HTML para o relatório. Podemos ter tantos modelos para quantas forem as necessidades de projeto.

# In[4]:


# carregamento do modelo
html_report_template = '../dw/reporting/report_template.html'


# - Por fim, escrevemos uma função de utilidade para converter o conteúdo de HTML para produzir o nosso PDF.

# In[5]:


# função de utilidade para conversão
def html_to_pdf(html_in, pdf_out):
    
    # arquivo de saída
    outfile = open(pdf_out, 'w+b')

    # conversão
    c = pisa.CreatePDF(html_in, dest=outfile)

    # fecha arquivo
    outfile.close()

    # retorna True se houver erro; False, senão
    return c.err


# - A execução da função de utilidade é melhor disposta em _script_. Aqui para fins de demonstração, o meio é indiferente.
# 
# No código abaixo, fazemos uma leve inserção de conteúdo no _template_, modificando o código-fonte HTML e exportando a saída para o documento `dw-report.pdf`.

# In[6]:


if __name__ == "__main__":
    pisa.showLogging()
    
    # inserção de dado no modelo
    with open(html_report_template) as h:
        source_html = h.read()
        cutoff = re.search('(</body>)',source_html).span()[0]
        head = source_html[:cutoff]    
        tail = source_html[cutoff:]
        mid = html_data(df)    
        source_html = head + mid + tail
    
        html_to_pdf(source_html,'../dw/reporting/pdf-output/dw-report.pdf')
        


# _Obs._: parte deste material é fictício. Qualquer semelhança com nomes, pessoas, factos ou situações da vida real terá sido mera coincidência.

# 

# ## Referências
# 
# - [Documentação: `xhtml2pdf`](https://xhtml2pdf.readthedocs.io/en/latest/index.html)
# - [W3 Schools](https://www.w3schools.com/html/default.asp)
# - [Reportlab](https://docs.reportlab.com/reportlab/userguide/ch1_intro/)
