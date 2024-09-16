from sqlalchemy.orm import Session
from models import Database, Frequencia, ResponseBase

class FrequenciaService:
    def __init__(self, db_url: str) -> None:
        self.database = Database(db_url=db_url)

    def new_session(self) -> Session:
        return self.database.new_session()

    def get_frequencias(self):
        with self.new_session() as session:
            frequencias = session.query(Frequencia).all()
        return frequencias

    def add_frequencia(self, data: dict) -> ResponseBase:
        with self.new_session() as session:
            frequencia = Frequencia(
                area=data.get('area'),
                unidade_operacional=data.get('unidade_operacional'),
                frequencia=data.get('frequencia'),
                tempo_base_parada=data.get('tempo_base_parada'),
                janeiro=data.get('janeiro'),
                fevereiro=data.get('fevereiro'),
                marco=data.get('marco'),
                abril=data.get('abril'),
                maio=data.get('maio'),
                junho=data.get('junho'),
                julho=data.get('julho'),
                agosto=data.get('agosto'),
                setembro=data.get('setembro'),
                outubro=data.get('outubro'),
                novembro=data.get('novembro'),
                dezembro=data.get('dezembro'),
                descricao=data.get('descricao'),
                observacoes=data.get('observacoes'),
                tempo_previsto=data.get('tempo_previsto'),
                tempo_real=data.get('tempo_real'),
                diferencial_tempo=data.get('diferencial_tempo'),
            )
            session.add(frequencia)
            session.commit()

        return ResponseBase(
            statusCode=200,
            message="Frequência adicionada com sucesso"
        )

    def get_frequencias_by_filters(self, **kwargs):
        filter_map = {
            'area': Frequencia.area,
            'unidade_operacional': Frequencia.unidade_operacional,
            'frequencia': Frequencia.frequencia,
            'tempo_base_parada': Frequencia.tempo_base_parada,
            # Add more filters as needed
        }

        with self.new_session() as session:
            query = session.query(Frequencia)
            for filter_name, filter_value in kwargs.items():
                if filter_name in filter_map:
                    query = query.filter(filter_map[filter_name] == filter_value)
                else:
                    raise ValueError(f"Filter '{filter_name}' is not supported")
            frequencias = query.all()
        return frequencias
