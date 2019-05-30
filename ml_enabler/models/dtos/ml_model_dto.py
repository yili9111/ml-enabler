from schematics import Model
from schematics.types import StringType, BaseType, IntType, DateTimeType


class MLModelDTO(Model):
    """ Describes JSON of an ML Model """

    model_id = IntType(serialized_name='modelId')
    created = DateTimeType()
    name = StringType(required=True)
    source = StringType(required=True)
    dockerhub_url = StringType(serialized_name='dockerhubUrl')
    dockerhub_hash = StringType(serialized_name='dockerhubHash')


class PredictionDTO(Model):
    """ Describes JSON of a set of predictions from a model """

    prediction_id = IntType(serialized_name='predictionsId')
    created = DateTimeType()
    model_id = IntType(serialized_name='modelId', required=True)
    version = IntType(required=True)
    bbox = BaseType(required=True)
    predictions = BaseType(required=True)