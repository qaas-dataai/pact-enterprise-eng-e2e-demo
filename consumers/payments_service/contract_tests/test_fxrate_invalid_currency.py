from pact import Consumer, Provider
import requests

pact = Consumer('payments_service').has_pact_with(
    Provider('payments_service'), port=5000, pact_dir='../../../../pacts'
)

def test_fxrate_invalid_currency():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /fxrate/XYZ')
     .with_request(method='get', path='/fxrate/XYZ')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/fxrate/XYZ')
        assert res.status_code == 404
        assert res.json() == expected