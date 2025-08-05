""""
.py file contains the pytest functions and configure to running tests
"""
import os

def pytest_addoption(parser):
    parser.addoption('--env', action="store", default="stage", help="Environment to run [dev or stage]")

def pytest_configure(config):
    os.environ['env'] = config.getoption('env')