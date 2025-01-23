# XOR Encryption and Decryption with Python

This Python program demonstrates how XOR (exclusive OR) operation can be used to encrypt and decrypt a numeric value. The XOR operation is a simple yet effective technique in basic cryptography. Additionally, a Continuous Integration (CI) pipeline is included to automate testing the code.

## How It Works

The program uses the following logic:

1. **Encryption**: The XOR operation is performed between a `number` and a `key` to generate an encrypted value.
   - Formula: `Encrypted = Number ^ Key`

2. **Decryption**: The XOR operation is applied again between the `Encrypted` value and the same `key` to retrieve the original `number`.
   - Formula: `Decrypted = Encrypted ^ Key`

### Example

- **Input Values**:  
  - `Number = 54` (`110110` in binary)  
  - `Key = 106` (`1101010` in binary)  

- **Encryption**:  
  - `Encrypted = Number ^ Key = 54 ^ 106 = 92` (`1011100` in binary)

- **Decryption**:  
  - `Decrypted = Encrypted ^ Key = 92 ^ 106 = 54` (`110110` in binary)

### Output

The program outputs:
1. The original number and key.
2. The encrypted value.
3. The decrypted value to verify correctness.
