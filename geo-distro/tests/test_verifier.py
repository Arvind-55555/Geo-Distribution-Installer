import unittest
from geodistro.verifier import Verifier

class TestVerifier(unittest.TestCase):
    def test_verify(self):
        verifier = Verifier()
        self.assertTrue(verifier.verify("test-package"))

if __name__ == "__main__":
    unittest.main()
