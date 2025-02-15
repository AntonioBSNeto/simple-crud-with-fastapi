from sqlalchemy.orm import Session
import models, schemas

# Empresas
def get_empresas(db: Session):
    return db.query(models.Empresa).all()

def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    db_empresa = get_empresa(db, empresa_id)
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
    return db_empresa

# Obrigações Acessórias
def get_obrigacoes(db: Session):
    return db.query(models.ObrigacaoAcessoria).all()

def get_obrigacao(db: Session, obrigacao_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()

def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate):
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def delete_obrigacao(db: Session, obrigacao_id: int):
    db_obrigacao = get_obrigacao(db, obrigacao_id)
    if db_obrigacao:
        db.delete(db_obrigacao)
        db.commit()
    return db_obrigacao
