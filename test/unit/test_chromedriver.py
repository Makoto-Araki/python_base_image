def get_chromedriver_version():
    result = subprocess.run(
        ["chromedriver", "--version"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_chromedriver_version():
    version = get_chromedriver_version()
    assert "143.0.7499.169" in version