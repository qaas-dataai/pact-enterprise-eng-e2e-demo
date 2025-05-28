from pact import Consumer, Provider
import requests

pact = Consumer('billing_service').has_pact_with(
    Provider('billing_service'), port=5000, pact_dir='../../../../pacts'
)

def test_vendor_not_found():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /vendor/999')
     .with_request(method='get', path='/vendor/999')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/vendor/999')
        assert res.status_code == 404
        assert res.json() == expected