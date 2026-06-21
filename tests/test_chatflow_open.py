import pytest
import gzip
import json
from chatflow_open import ChatFlowOpen, Message

def test_import_data():
    chat_flow = ChatFlowOpen()
    data = [
        {'id': 1, 'text': 'Hello'},
        {'id': 2, 'text': 'World'}
    ]
    with open('test_data.json.gz', 'wb') as file:
        file.write(gzip.compress(json.dumps(data).encode()))
    result = chat_flow.import_data('test_data.json.gz')
    assert result['imported'] == 2
    assert result['total'] == 2
    assert result['duplicates'] == 0

def test_import_data_duplicates():
    chat_flow = ChatFlowOpen()
    data = [
        {'id': 1, 'text': 'Hello'},
        {'id': 1, 'text': 'Hello'}
    ]
    with open('test_data.json.gz', 'wb') as file:
        file.write(gzip.compress(json.dumps(data).encode()))
    result = chat_flow.import_data('test_data.json.gz')
    assert result['imported'] == 1
    assert result['total'] == 2
    assert result['duplicates'] == 1

def test_import_data_invalid_json():
    chat_flow = ChatFlowOpen()
    with open('test_data.json.gz', 'wb') as file:
        file.write(gzip.compress(b'Invalid JSON'))
    with pytest.raises(ValueError):
        chat_flow.import_data('test_data.json.gz')

def test_validate_schema():
    chat_flow = ChatFlowOpen()
    data = [
        {'id': 1, 'text': 'Hello'},
        {'id': 2, 'text': 'World'}
    ]
    assert chat_flow.validate_schema(data)

def test_validate_schema_missing_field():
    chat_flow = ChatFlowOpen()
    data = [
        {'id': 1},
        {'id': 2, 'text': 'World'}
    ]
    assert not chat_flow.validate_schema(data)
