from pact import Consumer, Provider
import requests

pact = Consumer('auth_service').has_pact_with(
    Provider('auth_service'), port=5000, pact_dir='../../../../pacts'
)

def test_department_invalid():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /department/999')
     .with_request(method='get', path='/department/999')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/department/999')
        assert res.status_code == 404
        assert res.json() == expected