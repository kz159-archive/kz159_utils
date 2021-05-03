from kz159_utils import Config


def test_config_properties():
    config = Config()
    config.init_postgres()

    assert config.get_service_name() == 'kz159_utils'
    assert config.postgres.dsn == "postgresql://postgres:postgres@localhost:5432/postgres"
    assert config.postgres.test_db_name == "postgres_test"


def test_config_change_variable():
    config = Config()
    config.init_postgres()

    with config.temp_variable("postgres.host", "example_host.org"):
        assert config.postgres.host == "example_host.org"
    assert config.postgres.host == "localhost"

    with config.temp_variable('LOG_LEVEL', 'test_level'):
        assert config.LOG_LEVEL == 'test_level'
    assert config.LOG_LEVEL == 'INFO'
