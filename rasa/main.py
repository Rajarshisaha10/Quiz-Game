import subprocess

process = subprocess.Popen(
    [
        'powershell',
        '-Command',
        '& .\\.venv\\Scripts\\Activate.ps1; rasa run --enable-api'
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    cwd='.'  # current directory
)
for line in process.stdout:
    print(line)
    if 'Rasa server is up and running.' in line:
        break


process = subprocess.Popen(
    [
        'powershell',
        '-Command',
        '& .\\.venv\\Scripts\\Activate.ps1; rasa run actions'
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    cwd='.'  # current directory
)
for line in process.stdout:
    print(line)
    if 'Action endpoint is up and running on http://0.0.0.0:5055' in line:
        break

process2 = subprocess.Popen(
    [
        'powershell',
        '-Command',
        '& .\\.venv\\Scripts\\Activate.ps1; python gui.py'
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    cwd='.'
)