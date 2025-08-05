import datetime
from pydantic import PositiveFloat
from sqlalchemy import DateTime, ForeignKey, Integer, String
from Aula_08.categorias.models import CategoriaModel
from Aula_08.centro_treinamento.models import CentroTreinamentoModel
from Aula_08.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(PositiveFloat, nullable=False)
    altura: Mapped[float] = mapped_column(PositiveFloat, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False) # type: ignore
    categoria: Mapped['CategoriaModel'] = relationship(back_populates = 'atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centrotreinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates = 'atleta')
    centrotreinamento_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))