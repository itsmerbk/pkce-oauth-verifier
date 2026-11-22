import base64, hashlib, secrets

def generate_pkce():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    return verifier, challenge

if __name__ == "__main__":
    v, c = generate_pkce()
    assert len(v) >= 43 and len(c) == 43
    print("[PASS] 078_pkce_oauth_verifier")
