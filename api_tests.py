from utils import jsonschema
from schemas import SCHEMA_FOR_DEVELOPDB, SCHEMA_FOR_TESTDB, SCHEMA_ERROR
from methods import ApiMethods
import sys
import traceback


def test_post_to_developdb():
    test = ApiMethods()
    r = test.send_post("Develop.mr_robot", "pLSjFbcXoE")
    try:
        if r.status_code == 200:
            assert r.status_code == 200
            assert r.headers.get('content-type').split(";")[0] == 'application/json'
            assert jsonschema.validate(r.json(), SCHEMA_FOR_DEVELOPDB) is None
            assert r.elapsed.total_seconds() < 1
        else:
            print(r.status_code)
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))


def test_post_to_testvpndb():
    test = ApiMethods()
    r = test.send_post("Test.vpn", "XVlBzgbaiC")
    try:
        if r.status_code == 200:
            assert r.status_code == 200
            assert r.headers.get('content-type').split(";")[0] == 'application/json'
            assert jsonschema.validate(r.json(), SCHEMA_FOR_TESTDB) is None
            assert r.elapsed.total_seconds() < 1
        else:
            print(r.status_code)
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

def test_error_db():
    test = ApiMethods()
    r = test.send_post("", "")
    try:
        if r.status_code == 400:
            assert r.status_code == 400
            assert r.headers.get('content-type').split(";")[0] == 'application/json'
            assert jsonschema.validate(r.json(), SCHEMA_ERROR) is None
            assert r.elapsed.total_seconds() < 1
            assert r.json().get('error') == "config model not present"
        else:
            print(r.status_code)
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

def test_error_record():
    test = ApiMethods()
    r = test.send_post("Develop.mr_robot", "")
    try:
        if r.status_code == 400:
            assert r.status_code == 400
            assert r.headers.get('content-type').split(";")[0] == 'application/json'
            assert jsonschema.validate(r.json(), SCHEMA_ERROR) is None
            assert r.elapsed.total_seconds() < 1
            assert r.json().get('error') == "record not found"
        else:
            print(r.status_code)
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))

test_post_to_developdb()
test_post_to_testvpndb()
test_error_db()
test_error_record()