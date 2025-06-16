#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Workshop_: _Data Reporting_ com `reportlab`

# ## Objetivos do workshop
# 
# - Apresentar o módulo `reportlab` para geração de PDFs;
# - Desenvolver _workflow_ básico para geração de relatórios automatizados incorporando figuras geradas pelo `plotly`.

# Como vimos no {numref}`Capítulo %s <cap:reporting-html>`, a geração automatizada de relatórios pode ser feita a partir de muitas ferramentas. 
# 
# Neste capítulo, exploraremos um _workflow_ mínimo para conversão de dados em PDFs utilizando `reportlab`.

# ## Ferramentas utilizadas
# 
# - Módulos Python
#     - `plotly`
#     - `reportlab`
#     - `os`

# ## _ReportLab_
# 
# _ReportLab_ é uma biblioteca construída em Python útil para as seguintes finalidades:
# 
# - geração dinâmica de PDF na web;
# - produção de relatórios corporativos em grande volume e publicação de dados;
# - acoplamento em outras aplicações, incluindo uma "linguagem de relatório" customizável;
# - embasar como sistema de construção, a geração de documentos complexos, com gráficos e tabelas para fins de contabilidade, análise estatística e também publicação científica;
# 
# A _ReportLab_ possui duas versões, uma comercial e outra aberta. A versão aberta, _ReportLab PDF Toolkit_ possui uma extensão [documentação](https://docs.reportlab.com/reportlab/userguide/ch1_intro/) com tutoriais compreensíveis.

# ### Instalação
# 
# Recomenda-se utilizar _pip_ com: `pip install reportlab`.

# ## _Workflow_ demonstrativo

# Este workflow primário estende as capacidades discutidas com o módulo `xhtml2pdf` e mostra como inserir figuras de alta qualidade geradas via `plotly` em um documento PDF.

# Começamos com as importações (_boilerplate_).

# In[1]:


import os
import plotly.express as px
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Em seguida, criamos uma função de utilidade para produzir as imagens no PDF.

# ```{admonition} Nota
# :class: important
# Os métodos `showPage` e `save` não devem ser ignorados, visto que são eles os responsáveis por inserir os elementos na página do PDF e fechar o buffer do arquivo.
# ```

# In[2]:


# Função de utilidade

def img_to_pdf(pdfout,imgout,x,y,
               keep_img=False,
               open_pdf=True):
    
    # Cria canvas no PDF
    c = canvas.Canvas(pdfout, pagesize=A4)

    # Insere imagem 
    c.drawImage(imgout,x,y,preserveAspectRatio=True)

    # Salva o PDF
    c.showPage()
    c.save()

    # Deleta a imagem de teste
    if not keep_img:
        os.remove(imgout)
    
    # Abre PDF para exibição
    if open_pdf:
        os.system(f'open {pdfout}')


# Definimos alguns diretórios.

# In[3]:


imgext = 'png' # formatos OK: png (melhor), jpg, eps
basedir = '../dw/reporting/'
pdfout = basedir + 'pdf-output/report.pdf'
imgout = os.path.join(basedir,'test.'+ imgext)


# ```{admonition} Nota
# :class: important
# A experiência mostra que os formatos PNG, JPG e EPS, nesta ordem, são as melhores opções para renderização das imagens.
# ```

# As figuras _plotly.express_ podem ser objetos genéricos da classe. 

# In[4]:


fig = px.line(x=[1, 2, 3],
              y=[4, 5, 6],
              width=400,
              height=400)
fig.write_image(imgout)


# Por fim, a imagem é posta no PDF pela chamada da função de utilidade.

# In[5]:


img_to_pdf(pdfout,imgout,120,300,
               keep_img=False,
               open_pdf=True)


# Com esses pequenos passos, já é possível abrir o PDF para verificação.

# ```{admonition} Curiosidade
# :class: dropdown
# Visto que o módulo `os` já foi importado, para abrir o arquivo PDF diretamente, em sistemas UNIX, bastaria chamar: `_ = os.system(f'open {pdfout}')`.
# ```
