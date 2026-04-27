# Standard variable in case of no argument
NB = rise/01-introducao-rise.ipynb

# Target to generate and create static slides
slide:
	jupyter nbconvert rise/$(NB) \
		--to slides \
		--post serve \
		--no-input \
		--no-prompt

# Help
help:
	@echo "Usage: make slide NB=nome_do_arquivo.ipynb"	