{-----------------------------------------------------------------------------
 Objetivo   > O objetivo desta unit � realizar o controle de planos inativos
 Cria��o    > 29/06/2022 - marcio.souza
 Atualiza��o>
 -----------------------------------------------------------------------------}
unit CPlanoInativo;

interface

uses
  SysUtils, Classes, Variants, MPSObjeto, MPSClasseNegocio,
  CComum, DB, DBClient, MPSSombraConex, MPSObjparams;

type
  TClassePlanoInativo = class(TClasseComum)
    cdsPrincipalCodPlano: TIntegerField;
    cdsPrincipalCodUsuario: TStringField;
    cdsPrincipalCodUsuarioAlteracao: TStringField;
    cdsPrincipalDataAlteracao: TDateTimeField;
    cdsPrincipalDataCriacao: TDateTimeField;
    cdsPrincipalDataFinal: TDateField;
    cdsPrincipalDataInicial: TDateField;
    cdsPrincipalObservacao: TStringField;
    procedure cdsPrincipalCodPlanoValidate(Sender: TField);
    procedure cdsPrincipalNewRecord(DataSet: TDataSet);
    procedure MServidorClasseAntesConfirmar(cliente: TMClienteClasse);
    procedure cdsPrincipalDataFinalValidate(Sender: TField);
  private
    // Declara��es private
  protected
    // Declara��es protected
  public
    // Declara��es public
    procedure ValidarPlano(aParams: IMObjParams);
  end; // class TClassePlanoInativo

implementation

uses CAssocModPlano, ConvMedExcept, CPlano;

{$R *.DFM}

{-----------------------------------------------------------------------------
 Objetivo   > Valida se o plano informado existe
 Cria��o    >
 Atualiza��o> 14/07/2022 - marcio.souza
            > alterado de ValidarEmClasse para valida��o manual por conta dos
            > testes unit�rios, o m�todo ValidarEmClasse n�o consegue
            > utilizar as sombras de testes para as classes necess�rias
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.cdsPrincipalCodPlanoValidate(Sender: TField);
var
  Plano: TClassePlano;
  msgErro: string;
begin
  inherited;
  if '' <> Sender.Text then begin
    Plano := TClassePlano(TClassePlano.NovoAtivo(nil));
    try
      Plano.Selecionar(nil, ParamValor('aCodPlano', Sender.Value));
      if 0 = Plano.ContagemRegistros then
        raise EConvMedErro.Create('O plano informado ('''+IntToStr(Sender.Value)+''') n�o existe.');
    finally
      Plano.Desativar;
      if '' <> msgErro then
        raise EConvMedErro.Create(msgErro);
    end;
  end;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Realizar preenchimento autom�tico dos campos
 Cria��o    > 29/06/2022 - marcio.souza
 Atualiza��o>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.cdsPrincipalNewRecord(DataSet: TDataSet);
begin
  inherited;
  AtributoPorNome('aCodUsuario').Valor := CodUsuLogin;
  AtributoPorNome('aDataCriacao').Valor := Now;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Realizar preenchimetno autom�tico dos campos
 Cria��o    > 29/06/2022 - marcio.souza
 Atualiza��o>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.MServidorClasseAntesConfirmar(
  cliente: TMClienteClasse);
var
  aParams: IMObjParams;
begin
  inherited;
  AtributoPorNome('aCodUsuarioAlteracao').Valor := CodUsuLogin;
  AtributoPorNome('aDataAlteracao').Valor := Now;
  aParams := ParamValor('aCodPlano', AtributoPorNome('aCodPlano').Valor).
             ParamValor('aDataInicial', AtributoPorNome('aDataInicial').Valor).
             ParamValor('aDataFinal',AtributoPorNome('aDataFinal').Valor);
  ValidarPlano(aParams);
end;

{-----------------------------------------------------------------------------
 Objetivo   > Validar o c�digo do plano em quest�o
 Observa��o > somente planos que n�o contenham benefici�rios ativos vinculados
            > poder�o ser inativados.
 Cria��o    > 30/06/2022 - marcio.souza
 Atualiza��o>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.ValidarPlano(aParams: IMObjParams);
var
  AssocModPlano: TClasseComum;
  msgErro: string;
begin
  // verifica se � necess�rio utilizar o parametro aDataFinal
  if aParams.Existe('aDataFinal') then begin
    if (aParams.ParamPorNome('aDataFinal').Nulo) or (0 = aParams.ParamPorNome('aDataFinal').Valor) then
      aParams.Remover('aDataFinal');
  end;

  if aparams.Existe('aCodPlano') then begin
    AssocModPlano := TClasseAssocModPlano.NovoAtivo(Self);
    try
      TClasseAssocModPlano(AssocModPlano).AssociadoAtivoPorPlano(aParams);
      if 0 < AssocModPlano.ContagemRegistros then
        msgErro := 'N�o � poss�vel Inativar o plano, pois existem Associados Ativos vinculados ao mesmo.';
    finally
      AssocModPlano.Desativar(nil);
      if '' <> msgErro then
        raise EConvMedErro.Create(msgErro);
    end;
  end;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Validar o c�digo do plano em quest�o
 Observa��o > somente planos que n�o contenham benefici�rios ativos vinculados
            > poder�o ser inativados.
 Cria��o    > 30/06/2022 - marcio.souza
 Atualiza��o>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.cdsPrincipalDataFinalValidate(
  Sender: TField);
begin
  inherited;
  if (0 <> cdsPrincipalDataFinal.Value) and (cdsPrincipalDataInicial.Value > cdsPrincipalDataFinal.Value) then
    raise EConvMedErro.Create('Data Final inv�lida (menor que a Data Inicial).');
end;

initialization
  ClassesNegocio.RegistrarClasse('ClassePlanoInativo', TClassePlanoInativo);
finalization
  ClassesNegocio.DesregistrarClasse('ClassePlanoInativo');
end.
