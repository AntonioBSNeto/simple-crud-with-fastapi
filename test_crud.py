import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from database import Base
import models, schemas, crud

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testando o CRUD de Empresa
def test_create_empresa(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    assert empresa.nome == "Empresa Teste"
    assert empresa.cnpj == "12.345.678/0001-99"

def test_get_empresas(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    crud.create_empresa(db_session, empresa_data)
    empresas = crud.get_empresas(db_session)
    assert len(empresas) == 1
    assert empresas[0].nome == "Empresa Teste"

def test_get_empresa(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    fetched_empresa = crud.get_empresa(db_session, empresa.id)
    assert fetched_empresa is not None
    assert fetched_empresa.nome == "Empresa Teste"

def test_delete_empresa(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    deleted_empresa = crud.delete_empresa(db_session, empresa.id)
    assert deleted_empresa is not None
    assert deleted_empresa.nome == "Empresa Teste"
    assert crud.get_empresa(db_session, empresa.id) is None


# Testando o CRUD de Obrigação Acessória
def test_create_obrigacao(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    obrigacao_data = schemas.ObrigacaoAcessoriaCreate(
        nome="Declaração de Imposto",
        periodicidade="anual",
        empresa_id=empresa.id
    )
    obrigacao = crud.create_obrigacao(db_session, obrigacao_data)
    assert obrigacao.nome == "Declaração de Imposto"
    assert obrigacao.empresa_id == empresa.id

def test_get_obrigacoes(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    obrigacao_data = schemas.ObrigacaoAcessoriaCreate(
        nome="Declaração de Imposto",
        periodicidade="anual",
        empresa_id=empresa.id
    )
    crud.create_obrigacao(db_session, obrigacao_data)
    obrigacoes = crud.get_obrigacoes(db_session)
    assert len(obrigacoes) == 1
    assert obrigacoes[0].nome == "Declaração de Imposto"

def test_get_obrigacao(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    obrigacao_data = schemas.ObrigacaoAcessoriaCreate(
        nome="Declaração de Imposto",
        periodicidade="anual",
        empresa_id=empresa.id
    )
    obrigacao = crud.create_obrigacao(db_session, obrigacao_data)
    fetched_obrigacao = crud.get_obrigacao(db_session, obrigacao.id)
    assert fetched_obrigacao is not None
    assert fetched_obrigacao.nome == "Declaração de Imposto"

def test_delete_obrigacao(db_session):
    empresa_data = schemas.EmpresaCreate(
        nome="Empresa Teste",
        cnpj="12.345.678/0001-99",
        endereco="Rua Teste, 123",
        email="teste@email.com",
        telefone="99999-9999"
    )
    empresa = crud.create_empresa(db_session, empresa_data)
    obrigacao_data = schemas.ObrigacaoAcessoriaCreate(
        nome="Declaração de Imposto",
        periodicidade="anual",
        empresa_id=empresa.id
    )
    obrigacao = crud.create_obrigacao(db_session, obrigacao_data)
    deleted_obrigacao = crud.delete_obrigacao(db_session, obrigacao.id)
    assert deleted_obrigacao is not None
    assert deleted_obrigacao.nome == "Declaração de Imposto"
    assert crud.get_obrigacao(db_session, obrigacao.id) is None
