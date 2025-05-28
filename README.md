# 📦 Pact Enterprise E2E Demo

This repository demonstrates **contract testing at scale** for enterprise-grade microservices using [Pact](https://docs.pact.io/). It showcases:

- ✅ 7 consumer microservices
- ✅ 5 provider microservices
- ✅ 5 descriptive Pact tests per consumer
- ✅ Flask-based provider mocks
- ✅ Pact verification scripts per provider
- ✅ CI pipeline via GitHub Actions
- ✅ Local development support with virtual environment

---

## 🧭 Architecture Overview

```
                Pact Broker (optional)
                        |
         +--------------+---------------+
         |                              |
    Pact Files (.json)         Pact Verification
         |                              ^
         v                              |
+--------+--------+             +-------+--------+
|     Consumers    | ----------> |     Providers    |
| (Revenue, Auth,  | Pact tests  | (Employee, Dept, |
|  Billing, etc.)  | --------->  |  FX, Vendor...)  |
+------------------+             +------------------+
```

---

## 🗂️ Project Structure

```
.
├── consumers/
│   ├── revenue_service/
│   ├── billing_service/
│   ├── auth_service/
│   ├── payments_service/
│   ├── people_service/
│   ├── reports_service/
│   └── compliance_service/
│       └── contract_tests/
├── providers/
│   ├── employee_service/
│   ├── department_service/
│   ├── fxrate_service/
│   ├── vendor_service/
│   └── periodclose_service/
│       ├── app.py
│       └── verify_contracts.py
├── pacts/                     # Pact JSON files will be saved here
├── requirements.txt
├── setup_venv.sh
├── .github/
│   └── workflows/
│       └── contract-ci.yml
└── README.md
```

---

## 🛠️ Setup Instructions

1. **Set up your virtual environment:**

```bash
bash setup_venv.sh
```

This will:
- Create `venv/`
- Install `flask`, `requests`, `pact-python`, and `pytest`

2. **Run a provider service locally:**

```bash
python providers/employee_service/app.py
```

3. **Run consumer contract tests:**

```bash
pytest consumers/revenue_service/contract_tests
```

4. **Verify contracts against a provider:**

```bash
python providers/employee_service/verify_contracts.py
```

---

## 🔄 CI Integration

GitHub Actions is configured to:

- Install dependencies
- Run all consumer contract tests
- Run all provider contract verifications

See: `.github/workflows/contract-ci.yml`

---

## 🧪 Example Pact Test

```python
def test_employee_basic_profile():
    expected = {"id": 1, "name": "Alice", "role": "Engineer"}
    (pact
     .given('Valid state')
     .upon_receiving('a request for /employee/1')
     .with_request(method='get', path='/employee/1')
     .will_respond_with(status=200, body=expected))

    with pact:
        res = requests.get('http://localhost:5000/employee/1')
        assert res.status_code == 200
        assert res.json() == expected
```

---

## 🔍 What's Tested

Each consumer contract test:
- Sends a request to a mocked provider
- Verifies the response shape, values, and status
- Generates a pact file saved in `/pacts/`

Each provider:
- Is a simple Flask server
- Is validated using `verify_contracts.py` and `pact-verifier`

---

## ✅ Services Covered

### Consumers
- `revenue_service`
- `billing_service`
- `auth_service`
- `payments_service`
- `people_service`
- `reports_service`
- `compliance_service`

### Providers
- `employee_service`
- `vendor_service`
- `department_service`
- `fxrate_service`
- `periodclose_service`

---

## 📈 Potential Enhancements

- Add a Pact Broker (local or [Pactflow.io](https://pactflow.io))
- Enable `can-i-deploy` CI gate checks
- Add JSON schema validation
- Use matchers (`EachLike`, `Like`, etc.)
- Versioned APIs with consumer tags

---

##Contributing

This is a demo project. Feel free to extend test coverage, enhance CI/CD integration, or plug it into a real Pact Broker.

---

## 🧑‍💻 Maintainer Santhosh

Built for microservices quality engineering demos and internal POCs.
