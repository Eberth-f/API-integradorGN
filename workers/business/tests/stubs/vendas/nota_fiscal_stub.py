# -*- coding: utf-8 -*-

from datetime import datetime

from manager.business.models.nota_fiscal import NotaFiscal


class NotaFiscalStub:

    @classmethod
    def get_nota_fiscal_model(cls, empresa) -> NotaFiscal:
        return NotaFiscal(
            modelo=55,
            serie=1,
            numero=123,
            empresa=empresa,
            data_emissao=datetime.now().date().strftime('%Y-%m-%d')
        )

    @classmethod
    def get_gera_nota_fiscal_criar_task_contract(cls, nota_fiscal: object) -> dict:
        return dict(
            command=dict(
                task_name='GeraNotaFiscalCriar',
                params=dict(),
                data=dict(
                    modelo=nota_fiscal.modelo,
                    serie=nota_fiscal.serie,
                    numero=nota_fiscal.numero,
                    codigo_gera=nota_fiscal.empresa.codigo_gera,
                    data_emissao=nota_fiscal.data_emissao
                )
            )
        )
