# (C) Heikki Kupiainen 2023    

from typing import List
from pydantic import BaseModel, StrictStr

from api import Api
class StringDataset(BaseModel):
  items: List[List[StrictStr]]
  
  @staticmethod
  def build_from_text8():
    items = Api.load_text8_dataset()
    return StringDataset(**{
      'items': items
    })

def test_build_from_text8():
  dataset = StringDataset.build_from_text8()
  assert(type(dataset)) == StringDataset
  
def test_instantiation():
  assert(type((StringDataset(**{
    'items': [
      ['list', 'of', 'words']
    ]
  })))) == StringDataset