from ninja import ModelSchema, Schema
from .models import Livros

class LivrosSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nome', 'streaming', 'categorias']

class LivrosViewSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nome', 'streaming', 'categorias', 'id']

class AvaliacaoSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['nota', 'comentarios']

class FiltrosSortear(Schema):
    nota_minima: int = None
    categorias: int = None
    reler: bool = False 