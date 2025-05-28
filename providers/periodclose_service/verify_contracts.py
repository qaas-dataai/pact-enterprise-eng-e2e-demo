import subprocess

subprocess.run([
    'pact-verifier',
    '--provider-base-url=http://localhost:5000',
    '--pact-url=../../pacts/periodclose_service.json'
])
