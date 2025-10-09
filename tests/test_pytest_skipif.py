import pytest

System_Version = 'v1.2.0'


@pytest.mark.skipif(
    System_Version == 'v1.3.0',
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    System_Version == 'v1.2.0',
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():
    ...
