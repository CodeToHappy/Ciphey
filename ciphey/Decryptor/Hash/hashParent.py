try:
    from Decryptor.Hash import hashBuster
except ModuleNotFoundError:
    from ciphey.Decryptor.Hash import hashBuster


class HashParent:
    def decrypt(self, text):
        result = hashBuster.crack(text)
        return result

    def setProbTable(self, val):
        pass