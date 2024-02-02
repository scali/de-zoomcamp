if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date 

    print(data['vendor_id'].unique())
    print('Preprocessing: row with zero passengers: %i' % (data['passenger_count'].isin([0]).sum()))
    print('Preprocessing: row with trip distance equals to zero: %i' % (data['trip_distance'].isin([0]).sum()))
        
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are ride with 0 passengers'

@test
def test_trip_distance(output, *args) -> None:    
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are ride with a trip distance equals to zero'

@test
def test_vendor_id(output, *args) -> None:  


    expected = [2, 1]
    result = output['vendor_id'].unique()
    #print(expected)
    #print(result)
    
    assert (expected==result).all(), 'There are ride with a trip distance equals to zero'


