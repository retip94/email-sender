import pytest
from email_sender import main


@pytest.mark.parametrize('valid', ['testmail@gmail.com', 'test.me@check.me', 'Am.I.VALID@yes.com', ])
@pytest.mark.parametrize('not_valid', ['gmail.com', 'sdfasdf', 'sdf!@gmail.com', float('nan')])
def test_email_validation(valid, not_valid):
    assert main.validate_email(valid)
    assert not main.validate_email(not_valid)
