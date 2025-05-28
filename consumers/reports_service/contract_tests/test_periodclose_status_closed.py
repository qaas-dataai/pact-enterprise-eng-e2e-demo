from pact import Consumer, Provider
import requests

pact = Consumer('reports_service').has_pact_with(
    Provider('reports_service'), port=5000, pact_dir='../../../../pacts'
)

def test_periodclose_status_closed():
    expected = {'status': 'closed'}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /period/2024Q1')
     .with_request(method='get', path='/period/2024Q1')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/period/2024Q1')
        assert res.status_code == 200
        assert res.json() == expected