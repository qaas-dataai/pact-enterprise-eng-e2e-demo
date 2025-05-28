from pact import Consumer, Provider
import requests

pact = Consumer('payments_service').has_pact_with(
    Provider('payments_service'), port=5000, pact_dir='../../../../pacts'
)

def test_fxrate_usd_lookup():
    expected = {'currency': 'USD', 'rate': 1.23}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /fxrate/USD')
     .with_request(method='get', path='/fxrate/USD')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/fxrate/USD')
        assert res.status_code == 200
        assert res.json() == expected