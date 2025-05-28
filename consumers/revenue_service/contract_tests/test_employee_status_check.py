from pact import Consumer, Provider
import requests

pact = Consumer('revenue_service').has_pact_with(
    Provider('revenue_service'), port=5000, pact_dir='../../../../pacts'
)

def test_employee_status_check():
    expected = {'id': 1, 'status': 'active'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /employee/1')
     .with_request(method='get', path='/employee/1')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/employee/1')
        assert res.status_code == 200
        assert res.json() == expected