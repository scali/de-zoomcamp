if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import re

@transformer
def transform(data, *args, **kwargs):

    #pattern = re.compile()
    print(data.columns)

    data.columns = list(map(camel_to_snake, data.columns))
  
    data.columns = (data.columns
                .str.lower()
             ) 

    return data            


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()