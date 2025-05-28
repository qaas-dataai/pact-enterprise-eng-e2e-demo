from pact import Consumer, Provider
import requests

pact = Consumer('reports_service').has_pact_with(
    Provider('reports_service'), port=5000, pact_dir='../../../../pacts'
)

def test_periodclose_invalid_period():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /period/invalid')
     .with_request(method='get', path='/period/invalid')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/period/invalid')
        assert res.status_code == 404
        assert res.json() == expected