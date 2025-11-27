import base64
import os
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac

# ==========================================
#   KEY DERIVATION (FROM MASTER PASSWORD)
# ==========================================

def generate_key_from_master(master_password: str, salt: bytes) -> bytes:
    """
    Takes the user's master password and a random salt,
    returns a secure AES-256 key using PBKDF2.
    """
    key = pbkdf2_hmac(
        hash_name='sha256',
        password=master_password.encode(),
        salt=salt,
        iterations=390000,     # Strong recommended amount
        dklen=32               # 32 bytes = 256-bit AES key
    )
    return base64.urlsafe_b64encode(key)


# ==========================================
#   ENCRYPTION
# ==========================================

def encrypt_password(master_password: str, plain_password: str) -> str:
    """
    Encrypts the password using a key derived from the user's master password.
    Returns: base64 string containing salt + encrypted data.
    """
    # Generate random salt (needed for key derivation)
    salt = os.urandom(16)

    # Derive the encryption key from master password + salt
    key = generate_key_from_master(master_password, salt)

    f = Fernet(key)
    token = f.encrypt(plain_password.encode())

    # Store salt + encrypted token together (needed for decryption)
    encrypted_blob = base64.b64encode(salt + token).decode()

    return encrypted_blob


# ==========================================
#   DECRYPTION
# ==========================================

def decrypt_password(master_password: str, encrypted_blob: str) -> str:
    """
    Reverses encrypt_password() and returns the original password.
    """
    data = base64.b64decode(encrypted_blob)

    # Extract salt (first 16 bytes)
    salt = data[:16]
    token = data[16:]

    # Recreate key
    key = generate_key_from_master(master_password, salt)
    f = Fernet(key)

    plain = f.decrypt(token)

    return plain.decode()
