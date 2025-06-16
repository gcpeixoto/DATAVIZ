#!/usr/bin/env python
# coding: utf-8

# # Referências internas no JB
# 
# ## Seções
# 
# - Label
(sec:nome-secao)=
# Seção
# - Chamada
{numref}`Seção %s <sec:nome-secao>`.
# ## Figuras
# 
# - Bloco
```{figure} path/file-name.x
---
name: fig-name
alt: About it.
align: center
width: 500px
---
Caption here 
```
# - Chamada
{numref}`fig-name`
# ## Tabelas
# 
# - Bloco
```{table} Caption.
:name: tbl-name

| A | B | 
|:--|--:|
| a | b |
```
# - Chamada
{numref}`Tabela %s <tbl-name>`
# ## Citações
# 
# - Tendo o `refs.bib` com as devidas keys, cite com:
{cite:p}`refkey` # verifique outros modos além de cite:p
# ## Referências bibliográficas por capítulo
# 
# - No final do capítulo, use:
```{bibliography}
:filter: docname in docnames
```