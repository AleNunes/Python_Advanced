#!/bin/bash

# Script de conversao de LibreOffice para 4Slider

QTD=$(ls img*.png | wc -l)
NUM=$( expr $QTD - 1 )

for SLIDE in $(seq 0 $NUM)
do
  echo Slide $SLIDE
   #sed -i -e '1,10d' text$SLIDE.html
   sed -i -e 's/style="direction:ltr;"//' text$SLIDE.html
   sed -i -e 's/<font color="#333333">//' text$SLIDE.html
   sed -i -e 's/<\/font>//' text$SLIDE.html

#   NOTA=$(grep -n "<h3>Notas:</h3>" text$SLIDE.html | cut -d: -f1)
#   END=$(wc -l text$SLIDE.html | awk '{print $1}')
#   FIM=$( expr $END - 1 )
#   if [ ! -z $NOTA ]
#   then
#   sed "$NOTA","$FIM"'!d' text$SLIDE.html > notas$SLIDE.html
#   fi

 # Extrai o número da linha onde se inicia a parte de notas do arquivo .html
   NOTA=$(grep -n "<h3>Notas:</h3>" text$SLIDE.html | cut -d: -f1)
   # Extrai o número da linha onde se inicia o corpo do arquivo .html, baseando-se pelo primeiro "header" do corpo da página. 
   CORPO=$(cat -n text$SLIDE.html | egrep '<h[1-6]' | head -n1 | awk '{print $1}')
   # Extrai o número da última linha do arquivo .html
   END=$(cat -n text$SLIDE.html | tail -n1 | awk '{print $1}')
   
   # Pega o cabeçalho do arquivo .html e joga para um arquivo
   sed 1,"$( expr $CORPO - 1)"'!d' text$SLIDE.html > headers$NUM.html

   # Verifica se a variável NOTA é diferente de zero. Se for, pega as notas do arquivo .html e joga para um arquivo. Se não, não cria o arquivo.
   if [ ! -z $NOTA ]
   then
   	sed "$NOTA","$END"'!d' text$SLIDE.html > notas$SLIDE.html
   	FIM_CORPO=$NOTA
   else
   	FIM_CORPO=$END
   fi

   # Pega o corpo do arquivo .html e joga para um arquivo.
   sed "$CORPO","$( expr $FIM_CORPO - 1)"'!d'  text$SLIDE.html > terminal$SLIDE.html

   # Verifica se o corpo do arquivo é maior que 3 linhas e, se for, mantém o arquivo criado. Se não, apaga o arquivo criado.
   if [ $(cat -n terminal$SLIDE.html | tail -n1 | awk '{print $1}') -gt 3 ]
   then
   	echo "O arquivo foi mantido"
   else
   	echo "O arquivo sera excluido..."
	rm -f terminal$SLIDE.html
   fi
done
