from pact import Consumer, Provider
import requests

pact = Consumer('billing_service').has_pact_with(
    Provider('billing_service'), port=5000, pact_dir='../../../../pacts'
)

def test_vendor_active_status():
    expected = {'id': 22, 'active': True}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /vendor/22')
     .with_request(method='get', path='/vendor/22')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/vendor/22')
        assert res.status_code == 200
        assert res.json() == expected