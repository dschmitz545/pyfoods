

def test_app_is_created(app):  # injeção de depêndencia
    assert app.name == "pyfoods.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    assert client.get("/url_que_nao_existe").status_code == 404
