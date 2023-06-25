from BaseModel.MainModel import Main
from BaseModel.Marriage import Marriage

def searchBase(*, base):
    if base == 'main': return Main
    if base == 'marry': return Marriage