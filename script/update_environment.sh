#!/bin/zsh
# Exports environment.yml through conda and prepends help infor.

OUT="environment.yml"
echo "Exporting $OUT..."
conda env export > environment.yml

if [ $? -eq 0 ]; then
    echo "Done. Prepending header text..."
fi

HEADER="# Use this file for detailed environment creation through conda:
# conda env create --name env_name --file environment.yml
#
# Modify the prefix herein or pass it as argument with:
# conda env create --name env_name --file environment.yml --prefix path/where/install
#
# Use this for recreation after any additions
# conda env export > environment.yml"

echo -e "$HEADER\n$(cat environment.yml)" > environment.yml && mv environment.yml ../.

echo "environment.yml recreated on root."


