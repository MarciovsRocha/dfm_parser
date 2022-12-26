{-----------------------------------------------------------------------------
 Objetivo   > O objetivo desta unit é realizar o controle de planos inativos
 Criação    > 29/06/2022 - marcio.souza
 Atualização>
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
    // Declarações private
  protected
    // Declarações protected
  public
    // Declarações public
    procedure ValidarPlano(aParams: IMObjParams);
  end; // class TClassePlanoInativo

implementation

uses CAssocModPlano, ConvMedExcept, CPlano;

{$R *.DFM}

{-----------------------------------------------------------------------------
 Objetivo   > Valida se o plano informado existe
 Criação    >
 Atualização> 14/07/2022 - marcio.souza
            > alterado de ValidarEmClasse para validação manual por conta dos
            > testes unitários, o método ValidarEmClasse não consegue
            > utilizar as sombras de testes para as classes necessárias
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
        raise EConvMedErro.Create('O plano informado ('''+IntToStr(Sender.Value)+''') não existe.');
    finally
      Plano.Desativar;
      if '' <> msgErro then
        raise EConvMedErro.Create(msgErro);
    end;
  end;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Realizar preenchimento automático dos campos
 Criação    > 29/06/2022 - marcio.souza
 Atualização>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.cdsPrincipalNewRecord(DataSet: TDataSet);
begin
  inherited;
  AtributoPorNome('aCodUsuario').Valor := CodUsuLogin;
  AtributoPorNome('aDataCriacao').Valor := Now;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Realizar preenchimetno automático dos campos
 Criação    > 29/06/2022 - marcio.souza
 Atualização>
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
 Objetivo   > Validar o código do plano em questão
 Observação > somente planos que não contenham beneficiários ativos vinculados
            > poderão ser inativados.
 Criação    > 30/06/2022 - marcio.souza
 Atualização>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.ValidarPlano(aParams: IMObjParams);
var
  AssocModPlano: TClasseComum;
  msgErro: string;
begin
  // verifica se é necessário utilizar o parametro aDataFinal
  if aParams.Existe('aDataFinal') then begin
    if (aParams.ParamPorNome('aDataFinal').Nulo) or (0 = aParams.ParamPorNome('aDataFinal').Valor) then
      aParams.Remover('aDataFinal');
  end;

  if aparams.Existe('aCodPlano') then begin
    AssocModPlano := TClasseAssocModPlano.NovoAtivo(Self);
    try
      TClasseAssocModPlano(AssocModPlano).AssociadoAtivoPorPlano(aParams);
      if 0 < AssocModPlano.ContagemRegistros then
        msgErro := 'Não é possível Inativar o plano, pois existem Associados Ativos vinculados ao mesmo.';
    finally
      AssocModPlano.Desativar(nil);
      if '' <> msgErro then
        raise EConvMedErro.Create(msgErro);
    end;
  end;
end;

{-----------------------------------------------------------------------------
 Objetivo   > Validar o código do plano em questão
 Observação > somente planos que não contenham beneficiários ativos vinculados
            > poderão ser inativados.
 Criação    > 30/06/2022 - marcio.souza
 Atualização>
 -----------------------------------------------------------------------------}
procedure TClassePlanoInativo.cdsPrincipalDataFinalValidate(
  Sender: TField);
begin
  inherited;
  if (0 <> cdsPrincipalDataFinal.Value) and (cdsPrincipalDataInicial.Value > cdsPrincipalDataFinal.Value) then
    raise EConvMedErro.Create('Data Final inválida (menor que a Data Inicial).');
end;

initialization
  ClassesNegocio.RegistrarClasse('ClassePlanoInativo', TClassePlanoInativo);
finalization
  ClassesNegocio.DesregistrarClasse('ClassePlanoInativo');
end.
