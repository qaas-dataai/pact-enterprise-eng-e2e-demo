from pact import Consumer, Provider
import requests

pact = Consumer('compliance_service').has_pact_with(
    Provider('compliance_service'), port=5000, pact_dir='../../../../pacts'
)

def test_fxrate_audit_not_found():
    expected = {'error': 'Not found'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /fxrate/audit/XYZ')
     .with_request(method='get', path='/fxrate/audit/XYZ')
     .will_respond_with(status=404, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/fxrate/audit/XYZ')
        assert res.status_code == 404
        assert res.json() == expected