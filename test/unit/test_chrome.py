import subprocess

def get_chrome_version():
    result = subprocess.run(
        ["google-chrome", "--version"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_chrome_version():
    version = get_chrome_version()
    assert "143.0.7499.169" in version