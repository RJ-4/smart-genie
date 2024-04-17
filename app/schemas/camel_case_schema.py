from pydantic import BaseModel
from humps import camelize


def to_camel(property_name):
    return camelize(property_name)


class CamelCaseSchema(BaseModel):

    class Config:
        populate_by_name = True
        alias_generator = to_camel
