# test command line arg --env
# custom configs based on dev or qa env
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'staging'
    
# asserts just for trying out test cases
# normally you would use the base_url depending on the env
