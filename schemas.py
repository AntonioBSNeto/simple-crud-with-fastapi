from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List, Optional
import enum

class PeriodicidadeEnum(str, enum.Enum):
    mensal = "mensal"
    trimestral = "trimestral"
    anual = "anual"

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: PeriodicidadeEnum

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int

class ObrigacaoAcessoriaOut(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int

    model_config = ConfigDict(from_attributes=True)

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaOut(EmpresaBase):
    id: int
    obrigacoes: List[ObrigacaoAcessoriaOut] = []

    model_config = ConfigDict(from_attributes=True)
