from utils.data_converters import hex_to_lsb_bits,lsb_bits_to_hex,string_to_lsb_bits,lsb_bits_to_string
from crypto_engine.grain_v2 import Grain128AEADv2
if __name__ == "__main__":
    #phase 1 test
    test_hex="0001"
    bits=hex_to_lsb_bits(test_hex)
    print(f"Hex: {test_hex} -> Bits: {bits}")
    reconstructed_hex=lsb_bits_to_hex(bits)
    print(f"Bits: {bits} ->Reconstructed Hex: {reconstructed_hex}")

    #phase 2 test
    test_key_hex="00000000000000000000000000000000"
    test_iv_hex="000000000000000000000000"
    key_bits=hex_to_lsb_bits(test_key_hex)
    iv_bits=hex_to_lsb_bits(test_iv_hex)
    # Initialize Grain128AEADv2 and load key and IV
    grain=Grain128AEADv2()
    grain.load_key_and_iv(key_bits,iv_bits)
    print("Before initialization:")
    print(f"NFSR (Hex): {lsb_bits_to_hex(grain.NFSR)}")
    print(f"LFSR (Hex): {lsb_bits_to_hex(grain.LFSR)}\n")
    
    grain.initialise()
    print("After initialization:")
    print(f"NFSR (Hex): {lsb_bits_to_hex(grain.NFSR)}")
    print(f"LFSR (Hex): {lsb_bits_to_hex(grain.LFSR)}\n")

    # Encryption test
    plaintext="Hello, Grain!"
    print(f"Plaintext: {plaintext}")
    message_bits=string_to_lsb_bits(plaintext)
    ciphertext_bits=grain.encrypt(message_bits)
    print(f"Ciphertext (Hex): {lsb_bits_to_hex(ciphertext_bits)}")

    # Decryption test
    grain_decrypt=Grain128AEADv2()
    grain_decrypt.load_key_and_iv(key_bits,iv_bits)
    grain_decrypt.initialise()
    decrypted_bits=grain_decrypt.decrypt(ciphertext_bits)
    decrypted_text=lsb_bits_to_string(decrypted_bits)
    print(f"Decrypted Text: {decrypted_text}")