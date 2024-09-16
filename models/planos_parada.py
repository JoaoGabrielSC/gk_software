from sqlalchemy import Column, Integer, String
from models.base import Base

class Frequencia(Base):
    __tablename__ = 'frequencia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(50))
    unidade_operacional = Column(String(50))
    frequencia = Column(String(20))
    tempo_base_parada = Column(String(20))
    janeiro = Column(String(20))
    fevereiro = Column(String(20))
    marco = Column(String(20))
    abril = Column(String(20))
    maio = Column(String(20))
    junho = Column(String(20))
    julho = Column(String(20))
    agosto = Column(String(20))
    setembro = Column(String(20))
    outubro = Column(String(20))
    novembro = Column(String(20))
    dezembro = Column(String(20))
    descricao = Column(String(200))
    observacoes = Column(String(200))
    tempo_previsto = Column(String(20))
    tempo_real = Column(String(20))
    diferencial_tempo = Column(String(20))
