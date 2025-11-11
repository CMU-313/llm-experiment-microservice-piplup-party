from mock import patch
from src.llm import query_llm_robust, client


@patch.object(client, 'chat')
def test_unexpected_language(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.message.content = "I don't understand your request"

    # TODO assert the expected behavior
    assert query_llm_robust("Hier ist dein erstes Beispiel.")
    result = query_llm_robust("Hier ist dein erstes Beispiel.")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], bool)
    assert isinstance(result[1], str)
    assert result[1] != ""


@patch.object(client, 'chat')
def test_none_response(mocker):
    mocker.return_value.message.content = None
    out = query_llm_robust("Bonjour tout le monde")
    assert isinstance(out, tuple) and len(out) == 2
    assert isinstance(out[0], bool)
    assert isinstance(out[1], str) and out[1] != ""


@patch.object(client, 'chat')
def test_dict_response(mocker):
    mocker.return_value.message.content = {"text": "hola mundo"}
    out = query_llm_robust("Hola amigo")
    assert isinstance(out, tuple) and isinstance(out[1], str)


@patch.object(client, 'chat')
def test_model_raises(mocker):
    mocker.side_effect = Exception("service unavailable")
    out = query_llm_robust("Ciao mondo")
    assert isinstance(out, tuple) and len(out) == 2
    assert isinstance(out[0], bool)
    assert isinstance(out[1], str)

