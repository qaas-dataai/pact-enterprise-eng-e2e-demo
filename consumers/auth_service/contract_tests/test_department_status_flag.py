from pact import Consumer, Provider
import requests

pact = Consumer('auth_service').has_pact_with(
    Provider('auth_service'), port=5000, pact_dir='../../../../pacts'
)

def test_department_status_flag():
    expected = {'id': 42, 'disabled': False}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /department/42')
     .with_request(method='get', path='/department/42')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/department/42')
        assert res.status_code == 200
        assert res.json() == expected