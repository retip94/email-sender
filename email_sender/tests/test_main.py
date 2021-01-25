import pytest
from email_sender import main


@pytest.mark.parametrize('valid', ['testmail@gmail.com', 'test.me@check.me', 'Am.I.VALID@yes.com'])
def test_validate_email1(valid):
    assert main.validate_email(valid)


@pytest.mark.parametrize('not_valid', ['gmail.com', 'sdfasdf', 'sdf!@gmail.com', float('nan')])
def test_validate_email2(not_valid):
    assert not main.validate_email(not_valid)
