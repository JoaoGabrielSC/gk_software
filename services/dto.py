from pydantic import BaseModel
from typing import Optional

class FrequenciaDTO(BaseModel):
    area: str
    unidade_operacional: str
    frequencia: str
    tempo_base_parada: str
    janeiro: str
    fevereiro: str
    marco: str
    abril: str
    maio: str
    junho: str
    julho: str
    agosto: str
    setembro: str
    outubro: str
    novembro: str
    dezembro: str
    descricao: Optional[str] = None
    observacoes: Optional[str] = None
    tempo_previsto: Optional[str] = None
    tempo_real: Optional[str] = None
    diferencial_tempo: Optional[str] = None
