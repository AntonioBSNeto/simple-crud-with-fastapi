#from models import Empresa, ObrigacaoAcessoria

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Criar as tabelas no banco automaticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Simple CRUD API",
    description="API para gerenciamento de empresas e obrigações acessórias",
    version="1.0.0"
)

# Dependência para injeção de sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints para Empresas
@app.post("/empresas/", response_model=schemas.EmpresaOut, tags=["Empresas"], description="Cria uma nova empresa.")
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db, empresa)

@app.get("/empresas/", response_model=list[schemas.EmpresaOut], tags=["Empresas"], description="Lista todas as empresas.")
def list_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db)

@app.get("/empresas/{empresa_id}", response_model=schemas.EmpresaOut, tags=["Empresas"], description="Obtém uma empresa pelo ID.")
def get_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = crud.get_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.delete("/empresas/{empresa_id}", response_model=schemas.EmpresaOut, tags=["Empresas"], description="Deleta uma empresa pelo ID.")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = crud.delete_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

# Endpoints para Obrigações Acessórias
@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaOut, tags=["Obrigações Acessórias"], description="Cria uma nova obrigação acessória.")
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao(db, obrigacao)

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoriaOut], tags=["Obrigações Acessórias"], description="Lista todas as obrigações acessórias.")
def list_obrigacoes(db: Session = Depends(get_db)):
    return crud.get_obrigacoes(db)

@app.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoriaOut, tags=["Obrigações Acessórias"], description="Obtém uma obrigação acessória pelo ID.")
def get_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = crud.get_obrigacao(db, obrigacao_id)
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return obrigacao

@app.delete("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoriaOut, tags=["Obrigações Acessórias"], description="Deleta uma obrigação acessória pelo ID.")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = crud.delete_obrigacao(db, obrigacao_id)
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return obrigacao
