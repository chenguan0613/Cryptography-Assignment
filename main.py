import secrets
from utils.data_converters import hex_to_lsb_bits,lsb_bits_to_hex,string_to_lsb_bits,lsb_bits_to_string
from crypto_engine.grain_v2 import Grain128AEADv2
from key_management.wrapper import KeyManager
from file_io.file_handler import FileHandler
import json
if __name__ == "__main__":
    key_manager = KeyManager()
    password = "my_secure_password"
    ad_data = "student_id:12345"
    real_grain_key = KeyManager.generate_random_key_hex()
    test_iv_hex = secrets.token_hex(12)
    test_ciphertext_hex = "a1b2c3d4e5f607080910"
    test_plaintext = "Hello, XMUM Cyber Security!"
    print("Generated Grain Key (Hex):", real_grain_key)
    print("Generated IV (Hex):", test_iv_hex)
    real_key_dict = key_manager.wrap_key(password, real_grain_key, ad_data, ad_is_hex=False)
    FileHandler.save_key_file(real_key_dict, "real_test.key")
    FileHandler.save_encrypted_file(test_iv_hex, test_ciphertext_hex, "real_test.enc")
    FileHandler.save_decrypted_file(test_plaintext, "real_test.dec")
    recovered_iv, recovered_cipher = FileHandler.load_encrypted_file("real_test.enc")
    if recovered_iv == test_iv_hex and recovered_cipher == test_ciphertext_hex:
        print("🎉 全链路测试完美通过！阶段三生成的真实数据已成功通过阶段四落盘。")
    else:
        print("❌ 测试失败！")