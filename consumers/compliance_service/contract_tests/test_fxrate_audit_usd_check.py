from pact import Consumer, Provider
import requests

pact = Consumer('compliance_service').has_pact_with(
    Provider('compliance_service'), port=5000, pact_dir='../../../../pacts'
)

def test_fxrate_audit_usd_check():
    expected = {'currency': 'USD'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /fxrate/audit/USD')
     .with_request(method='get', path='/fxrate/audit/USD')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/fxrate/audit/USD')
        assert res.status_code == 200
        assert res.json() == expected