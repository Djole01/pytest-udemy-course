from pytest import fixture
from config import Config

# command line arg --env
def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests against")





# get command line arg
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


# set command line arg to a variable
@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
