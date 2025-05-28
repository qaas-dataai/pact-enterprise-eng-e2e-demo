from pact import Consumer, Provider
import requests

pact = Consumer('revenue_service').has_pact_with(
    Provider('revenue_service'), port=5000, pact_dir='../../../../pacts'
)

def test_employee_missing_fallback():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /employee/404')
     .with_request(method='get', path='/employee/404')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/employee/404')
        assert res.status_code == 404
        assert res.json() == expected