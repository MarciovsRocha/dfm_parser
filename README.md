# DFM Parser

Este projeto l� um arquivo DFM (Delphi Form)
e extrai algumas informa��es declaradas neste
arquivo, e.g.: Atributos/Fields.

## How to

Informar o caminho absoluto do arquivo DFM no
m�todo construtor do objeto `DFMParser`
para que a inst�ncia criada consiga abri-lo.

Ap�s criada a inst�ncia basta executar o m�todo
`parse()` para que este extraia os dados do
arquivo DFM informado.

## Using Extract Data

Utilizar os dados extra�dos � poss�vel converter
um Objeto `Property` (declarado no arquivo classes.py)
para `JSON` pelo m�todo `Property.to_json()`.

Ou utilziar os m�todos da biblioteca de utilidades `utils.py`,
nesta biblioteca est�o implementados m�todos que manuseiam os
objetos `Property`, e.g.: `utils.CriarEstruturaLocal(lista_atributos, lista_fields)`

### Criar Estrutura Local (`utils.CriarEstruturaLocal`)

Para este m�toddo informe a lista de atributos obtida por `parser.get_lista_atributos()`
e a lista de fields obtida por `parser.get_lista_fields()`,
O retorno do m�todo `utils.CriarEstruturaLocal` ser� uma string
de defini��es para todos os atributos, encontrados no arquivo
serializado pelo `DFMParser`, pronta para ser concatenada ao m�todo
da sombra de teste `TSombraTeste.CriarEstruturaLocal`.
