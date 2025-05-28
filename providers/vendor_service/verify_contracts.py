import subprocess

subprocess.run([
    'pact-verifier',
    '--provider-base-url=http://localhost:5000',
    '--pact-url=../../pacts/vendor_service.json'
])
