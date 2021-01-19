from os.path import join, dirname
import json
from datetime import datetime


def load_test_data_json():
    """ Loads test data json file """
    absolute_path = join(dirname(__file__), 'test_data.json')
    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())


class TestData(object):

    def __init__(self, registration_form):
        test_data = load_test_data_json()
        self.firstName = test_data[registration_form]["firstName"]
        self.lastName = test_data[registration_form]["lastName"]
        self.companyName = test_data[registration_form]["companyName"]
        self.email = test_data[registration_form]["email"] + str(datetime.now())[17:26] + test_data[registration_form]["emailDomain"]
        self.phone = test_data[registration_form]["phone"]
        self.jobTitle = test_data[registration_form]["jobTitle"]
        self.companyType = test_data[registration_form]["companyType"]

