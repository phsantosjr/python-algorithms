class CaesarCipher:
    """
    Class for doing encryption and decryption using Caesar Cipher

    Explanation: https://en.wikipedia.org/wiki/Caesar_cipher

    Source: Data Structures and Algorithms in Python
    """

    def __init__(self, shift: int):
        encoder = [None] * 26       # temp array for encryption
        decoder = [None] * 26       # temp array for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))

        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message: str) -> str:
        """
        Return string representing encripted messat
        :param message: text with a message to encrypt
        :return: encrypt message
        """
        return self._transform(message, self._forward)

    def decrypt(self, secret: str) -> str:
        """
        Return decrypted message given encrypted message
        :param secret: message encrypted
        :return: message decrypted
        """
        return self._transform(secret, self._backward)

    def _transform(self, original: str, code: str) -> str:
        """
        Utility to perform transformation based on given code string
        :param original: message to encrypt or decrypt
        :param code: code to use in encrypt/decrypt process
        :return:
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = code[j]
        return "".join(msg)
