from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlanosParada(Base):
    __tablename__ = 'frequencia'

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String, index=True)
    unidade_operacional = Column(String)
    frequencia = Column(String)
    tempo_base_parada = Column(String)
    janeiro = Column(String)
    fevereiro = Column(String)
    marco = Column(String)
    abril = Column(String)
    maio = Column(String)
    junho = Column(String)
    julho = Column(String)
    agosto = Column(String)
    setembro = Column(String)
    outubro = Column(String)
    novembro = Column(String)
    dezembro = Column(String)
    descricao = Column(String)
    observacoes = Column(String)
    tempo_previsto = Column(String)
    tempo_real = Column(String)
    diferencial_tempo = Column(String)
