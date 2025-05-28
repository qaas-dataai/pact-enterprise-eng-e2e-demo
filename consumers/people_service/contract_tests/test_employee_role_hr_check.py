from pact import Consumer, Provider
import requests

pact = Consumer('people_service').has_pact_with(
    Provider('people_service'), port=5000, pact_dir='../../../../pacts'
)

def test_employee_role_hr_check():
    expected = {'role': 'HR Manager'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /employee/2')
     .with_request(method='get', path='/employee/2')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/employee/2')
        assert res.status_code == 200
        assert res.json() == expected