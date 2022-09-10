import pytest
import rich

@pytest.fixture()
def blue(request, capsys):
    def _blue(text: str):
        with capsys.disabled():
            test_func = request.node.nodeid
            rich.print(f'\n[blue]----- {test_func}: {text}')
    return _blue