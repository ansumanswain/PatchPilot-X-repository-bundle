from app.auth import validate_email

def test_email_validation():
    assert validate_email("test@example.com")

def test_email_with_spaces():
    assert validate_email("  test@example.com  ")
