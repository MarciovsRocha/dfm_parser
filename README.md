# DFM Parser

Este projeto lê um arquivo DFM (Delphi Form)
e extrai algumas informações declaradas neste
arquivo, e.g.: Atributos/Fields.

## How to

Informar o caminho absoluto do arquivo DFM no
método construtor do objeto `DFMParser`
para que a instância criada consiga abri-lo.

Após criada a instância basta executar o método
`parse()` para que este extraia os dados do
arquivo DFM informado.

## Using Extract Data

Utilizar os dados extraídos é possível converter
um Objeto `Property` (declarado no arquivo classes.py)
para `JSON` pelo método `Property.to_json()`.

Ou utilziar os métodos da biblioteca de utilidades `utils.py`,
nesta biblioteca estão implementados métodos que manuseiam os
objetos `Property`, e.g.: `utils.CriarEstruturaLocal(lista_atributos, lista_fields)`

### Criar Estrutura Local (`utils.CriarEstruturaLocal`)

Para este métoddo informe a lista de atributos obtida por `parser.get_lista_atributos()`
e a lista de fields obtida por `parser.get_lista_fields()`,
O retorno do método `utils.CriarEstruturaLocal` será uma string
de definições para todos os atributos, encontrados no arquivo
serializado pelo `DFMParser`, pronta para ser concatenada ao método
da sombra de teste `TSombraTeste.CriarEstruturaLocal`.

Atualização 01/02/2023
