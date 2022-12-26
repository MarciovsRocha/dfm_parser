inherited ClassePlanoInativo: TClassePlanoInativo
  NomeClasse = 'ClassePlanoInativo'
  Atributos = <
    item
      DataSource = dtsPrincipal
      Nome = 'adPrincipal'
    end
    item
      DataType = ftInteger
      DataSource = dtsPrincipal
      DataField = 'CodPlano'
      Nome = 'aCodPlano'
    end
    item
      DataSource = dtsPrincipal
      DataField = 'CodUsuario'
      Nome = 'aCodUsuario'
    end
    item
      DataSource = dtsPrincipal
      DataField = 'CodUsuarioAlteracao'
      Nome = 'aCodUsuarioAlteracao'
    end
    item
      DataType = ftDateTime
      DataSource = dtsPrincipal
      DataField = 'DataAlteracao'
      Nome = 'aDataAlteracao'
    end
    item
      DataType = ftDateTime
      DataSource = dtsPrincipal
      DataField = 'DataCriacao'
      Nome = 'aDataCriacao'
    end
    item
      DataType = ftDate
      DataSource = dtsPrincipal
      DataField = 'DataFinal'
      Nome = 'aDataFinal'
    end
    item
      DataType = ftDate
      DataSource = dtsPrincipal
      DataField = 'DataInicial'
      Nome = 'aDataInicial'
    end
    item
      DataSource = dtsPrincipal
      DataField = 'Observacao'
      Nome = 'aObservacao'
    end>
  NomeServidor = 'ClassePlanoInativo'
  OnAntesConfirmar = MServidorClasseAntesConfirmar
  SemOwner = True
  inherited cdsPrincipal: TClientDataSet
    OnNewRecord = cdsPrincipalNewRecord
    object cdsPrincipalCodPlano: TIntegerField
      FieldName = 'CodPlano'
      OnValidate = cdsPrincipalCodPlanoValidate
    end
    object cdsPrincipalCodUsuario: TStringField
      FieldName = 'CodUsuario'
      Size = 8
    end
    object cdsPrincipalCodUsuarioAlteracao: TStringField
      FieldName = 'CodUsuarioAlteracao'
      Size = 8
    end
    object cdsPrincipalDataAlteracao: TDateTimeField
      FieldName = 'DataAlteracao'
    end
    object cdsPrincipalDataCriacao: TDateTimeField
      FieldName = 'DataCriacao'
    end
    object cdsPrincipalDataFinal: TDateField
      FieldName = 'DataFinal'
      OnValidate = cdsPrincipalDataFinalValidate
    end
    object cdsPrincipalDataInicial: TDateField
      FieldName = 'DataInicial'
    end
    object cdsPrincipalObservacao: TStringField
      FieldName = 'Observacao'
      Size = 255
    end
  end
end
