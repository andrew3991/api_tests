import jsonschema
from jsonschema.exceptions import ValidationError


def validate(obj, schema):
    try:
        v = jsonschema.validate(obj, schema)
    except ValidationError:
        v = "Error in validation"
    return(v)