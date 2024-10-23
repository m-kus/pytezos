from unittest import TestCase
from unittest.mock import patch

from mnemonic import Mnemonic
from parameterized import parameterized  # type: ignore

from pytezos.crypto.key import Key


class TestCrypto(TestCase):
    """
    Test data generation:
    ./tezos-client gen keys test_ed25519 -s ed25519 --force (--encrypted)
    ./tezos-client gen keys test_secp256k1 -s secp256k1 --force (--encrypted)
    ./tezos-client gen keys test_p256 -s p256 --force (--encrypted)
    ./tezos-client show address test_ed25519 -S
    ./tezos-client show address test_secp256k1 -S
    ./tezos-client show address test_p256 -S
    ./tezos-client sign bytes 0x74657374 for test_ed25519
    ./tezos-client sign bytes 0x74657374 for test_secp256k1
    ./tezos-client sign bytes 0x74657374 for test_p256

    Issues:
    * `tezos-client sign bytes` does not support P256 curve
    """

    @parameterized.expand(
        [
            (
                'edsk3nM41ygNfSxVU4w1uAW3G9EnTQEB5rjojeZedLTGmiGRcierVv',
                'edpku976gpuAD2bXyx1XGraeKuCo1gUZ3LAJcHM12W1ecxZwoiu22R',
                'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq',
            ),
            (
                'spsk1zkqrmst1yg2c4xi3crWcZPqgdc9KtPtb9SAZWYHAdiQzdHy7j',
                'sppk7aMNM3xh14haqEyaxNjSt7hXanCDyoWtRcxF8wbtya859ak6yZT',
                'tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu',
            ),
            (
                'p2sk3PM77YMR99AvD3fSSxeLChMdiQ6kkEzqoPuSwQqhPsh29irGLC',
                'p2pk679D18uQNkdjpRxuBXL5CqcDKTKzsiXVtc9oCUT6xb82zQmgUks',
                'tz3agP9LGe2cXmKQyYn6T68BHKjjktDbbSWX',
            ),
            (
                'p2sk2rHNfHbuqq1Q6RZAnXfwoA3fFk1xtUFPrNVj7mhwxmvY4xmrEd',
                'p2pk663exKaDHnzFmUeBsmYjKUMJYPyW1WQJzmhyYgNrUuo5Ef9SXxG',
                'tz3VqqyCrvZni4jbxVrzG2EeVQ97D9LARjJz',
            ),
            (
                'p2sk2Md6rioE62a7hVdD8xdYGDLH2erDbAcD4i15e8DSpnHruhVHBw',
                'p2pk66yEDuRC5RLHpVj8hvAS5fr8HnU2YsLvFNdwQoW3jH8WUynMwGG',
                'tz3Q2KTKWw3xqiowvfX4N7gyyAfCz8hTvcnk',
            ),
            (
                'BLsk1ijYmTDL6hfUvrFCqgwbetg6FTpHLbzPDKLAfP9tB9Cej8dME5',
                'BLpk1q8T9TqRSNTacJU1WvTVtj62LZ8WZtGzZ3tQoQANzoXHwAPtxpJCY79TfoNu2m9N6RbFfh7s',
                'tz4F76GBmuLgXvUjLb2gfeBeM6fBf6EsuD1T',
            ),
            (
                'BLsk1X2dnEkx4KemkR5Q5j1agrstAfZxX1pXUVDLUCzg6bQfTXkv5u',
                'BLpk1mN7zNwSvC7KLkhJwUuWm4riPqtpCXDqT662Ffob3Vo3LcmCTfnkzo5LGFKG24L9xG3d1SeW',
                'tz4MQK3m8tqP7RrvZixbyGjY4BGRXp52XMVW',
            ),
        ]
    )
    def test_derive_key_data(self, sk, pk, pkh):
        public_key = Key.from_encoded_key(pk)
        assert not public_key.is_secret
        assert pk == public_key.public_key()
        assert pkh == public_key.public_key_hash()

        secret_key = Key.from_encoded_key(sk)
        assert secret_key.is_secret
        assert sk == secret_key.secret_key()
        assert pk == secret_key.public_key()
        assert pkh == secret_key.public_key_hash()

    @parameterized.expand(
        [
            (
                'edpku976gpuAD2bXyx1XGraeKuCo1gUZ3LAJcHM12W1ecxZwoiu22R',
                b'test',
                'edsigtzLBGCyadERX1QsYHKpwnxSxEYQeGLnJGsSkHEsyY8vB5GcNdnvzUZDdFevJK7YZQ2ujwVjvQZn62ahCEcy74AwtbA8HuN',
            ),
            (
                'sppk7aMNM3xh14haqEyaxNjSt7hXanCDyoWtRcxF8wbtya859ak6yZT',
                b'test',
                'spsig1RriZtYADyRhyNoQMa6AiPuJJ7AUDcrxWZfgqexzgANqMv4nXs6qsXDoXcoChBgmCcn2t7Y3EkJaVRuAmNh2cDDxWTdmsz',
            ),
            (
                'p2pk67wVncLFS1DQDm2gVR45sYCzQSXTtqn3bviNYXVCq6WRoqtxHXL',
                '017a06a770000508440322bf4860a065d1c8747a08f7685be9c79da2b21d5930c12fff86b230081d223b000000005c752b3'
                'a04bc5b950ff781580616c12a646af98285da66232b232661f179c98d6f8c8912ae00000011000000010000000008000000'
                '00009b55bda7ad9debcd2657b76d444b14807c7b5dc13e06f754e2b43186d0fb22b3d3332c0000000000031048815b00',
                'sigqWxz3GKFXg6G8ndSzJF8JD9j7m12kPWZj6bHLqdKw6XpxhVLwGm26hVqMdEfgPdoz8qoA5QkM9mvnMyMFmYny9sqjb5bE',
            ),
            (
                'p2pk66n1NmhPDEkcf9sXEKe9kBoTwBoTYxke1hx16aTRVq8MoXuwNqo',
                '027a06a770ad828485977947451e23e99f5040ead0f09ef89f58be2583640edcb1e295d0cb000005085e',
                'sigQVTY9CkYw8qL6Xa7QWestkLSdtPv6HZ4ToSMHDcRot3BwRGwZhSwXd9jJwKkDvvotTLSNWQdUqiDSfXuCNUfjbEaY2j6j',
            ),
            (
                'BLsk1vhAKWY755ny1N1idqkzpHM4XpTEVdhybgDk3w4Lf2oFc4B5mU',
                b'bls12_381 verify external signature',
                'BLsigB2azuvvpWDifK3xCMGDXUcF17V1R7NGfKQsUVrzm7718uvbjtrXpS3KMq5CSJiAWAS9Rjj79Zak3TskGGwDGfHnm52rvdb9rpJxtyXK39FNadwGX4EGtqXVDge9eDRjSm8bVNxJE6',
            ),
        ]
    )
    def test_verify_ext_signatures(self, pk, msg, sig):
        key = Key.from_encoded_key(pk)
        key.verify(sig, msg)
        self.assertRaises(ValueError, key.verify, sig, b'fake')

    @parameterized.expand(
        [
            ('edsk3nM41ygNfSxVU4w1uAW3G9EnTQEB5rjojeZedLTGmiGRcierVv', '0xdeadbeaf'),
            ('spsk1zkqrmst1yg2c4xi3crWcZPqgdc9KtPtb9SAZWYHAdiQzdHy7j', b'hello'),
            ('p2sk3PM77YMR99AvD3fSSxeLChMdiQ6kkEzqoPuSwQqhPsh29irGLC', b'test'),
            ('BLsk2cZcs2umUhDAQVUxqZnEnaj5p7W7TeHh9dc6F1E3j1bnfRJtaR', b'bls12_381 sign and verify'),
        ]
    )
    def test_sign_and_verify(self, sk, msg):
        key = Key.from_encoded_key(sk)
        sig = key.sign(msg)
        key.verify(sig, msg)
        self.assertRaises(ValueError, key.verify, sig, b'fake')

    @parameterized.expand(
        [
            (
                'edsk3nM41ygNfSxVU4w1uAW3G9EnTQEB5rjojeZedLTGmiGRcierVv',
                b'test',
                'edsigtzLBGCyadERX1QsYHKpwnxSxEYQeGLnJGsSkHEsyY8vB5GcNdnvzUZDdFevJK7YZQ2ujwVjvQZn62ahCEcy74AwtbA8HuN',
            ),
            (
                'spsk1zkqrmst1yg2c4xi3crWcZPqgdc9KtPtb9SAZWYHAdiQzdHy7j',
                b'test',
                'spsig1RriZtYADyRhyNoQMa6AiPuJJ7AUDcrxWZfgqexzgANqMv4nXs6qsXDoXcoChBgmCcn2t7Y3EkJaVRuAmNh2cDDxWTdmsz',
            ),
            (
                'BLsk2FqWKU2Zs4Tio4L6keJfmRq8ZCvTqzCp2zy9x6VhE3aJgvVXjx',
                b'bls12_381 deterministic signatures',
                'BLsigA1NaMLRjBFBm1zK2JCgLt8Ku4mN9bipt6TtSNaTo7tsXNB9rWgjimvsc7vb9YjfXS31yt9zzpcNnBRVkgwkVBQFphLwhrrW3hnRPz58MZDPSPFZcn59ZBcYr8JLQpmpTZABjxzVfH',
            ),
        ]
    )
    def test_deterministic_signatures(self, sk, msg, sig):
        """
        See RFC6979 for explanation
        https://tools.ietf.org/html/rfc6979#section-3.2
        """
        key = Key.from_encoded_key(sk)
        signature = key.sign(msg)
        self.assertEqual(sig, signature)

    @parameterized.expand(
        [
            (
                'edesk1zxaPJkhNGSzgZDDSphvPzSNrnbmqes8xzUrw1wdFxdRT7ePiQz8D2Q18fMjn6fC9ZRS2rUbg8d8snxxznE',
                'qqq',
                b'\xf2h\xbb\xf5\xc7\xe2\xb9\x97',
                'edpktmNJub2v7tVjSU8nA9jZrdV5JezmFtZA4yd3jj18i6VKcCJzdo',
            ),
            (
                'spesk21cruoqtYmxfq5fpkXiZZRLRw4vh7VFJauGCAgHxZf3q6Q5LTv9m9dnMxyVjna6RzWQL45q4ppGLh97xZpV',
                'qqq',
                b'\xbe\xb8\xeefi\x14\\T',
                'sppk7Zbcqfy67b6pRMAKax5QKzAxTQUxmfQcCuvn1QMFQsXqy1NkSkz',
            ),
            (
                'p2esk1rqdHRPz4xQh8uP8JaWSVnGFTKxkh2utdjK5CPDTXAzzh5sXnnobLkGrXEZzGhCKFDSjv8Ggrjt7PnobRzs',
                'qqq',
                b'"\xf8\x0e \x0f]hc',
                'p2pk68Ky2h9UZZ4jUYws8mU8Cazhu4H1LdK22wD8HgDPRSvsJPBDtJ7',
            ),
            (
                'BLesk1a3e2vNGbbPV5rFRHZZCHvZEvvtGP5Puer4yRfRVLR8E1xVyk5owiUeudZcaa31mGDmvbr9LH6ZPTUdi66z',
                'qqq',
                b'q\xc1\x1e\xd4\x8f\xeby\xc8',
                'BLpk1kuaZeC775wf3VtwYXEipCVK1jkPdu7xcroNCw1kKci7ncaTRQ1ehCCpdiye1BugTMjWx1Xx',
            ),
        ]
    )
    def test_encrypted_keys(self, sk, passphrase, salt, pk):
        key = Key.from_encoded_key(sk, passphrase=passphrase)
        assert pk == key.public_key()

        with patch('pytezos.crypto.key.pysodium.randombytes', return_value=salt):
            assert sk == key.secret_key(passphrase)

    @parameterized.expand(
        [
            ('eight life cycle hub response suffer useless custom drama baby royal embrace door',),
            ('eight life cycle hub response suffer useless custom drama baby royal embrace door on tw',),
            ('eight life cycle hub response suffer useless custom drama baby royal embrace door duck dog',),
        ]
    )
    def test_bad_mnemonic(self, mnemonic):
        self.assertRaises(ValueError, Key.from_mnemonic, mnemonic)

    def test_french_mnemonic(self):
        # Ensure that English isn't the only language supported for loading keys
        mnemonic = Mnemonic('french').generate(128)
        self.assertIsNotNone(Key.from_mnemonic(mnemonic, validate=True, language='french'))

    def test_regression_p256_short_sig(self):
        key = Key.from_encoded_key('p2sk3xPfYsoExTVi7bGSH2KoHgpxFNqewUczHkLtQvr1bwnbhzGM9Y')
        key.sign('try25')

    def test_encrypted_key_str_password(self):
        key = Key.from_encoded_key(
            key='edesk1UrFQK6xJM6SYdLxMQbyKaaYQmzYVvQRpJXUmxj3apZ1ufRu4aHSTqWrJiqcHywSbnF146wkNcpUAW7Qy6H',
            passphrase='12345',
        )
        self.assertEqual('edsk2juUM8ZMUkaCKHWVnzWhp9DxrK93YK1rQjYk3pTEq2ThXpBxkX', key.secret_key())
