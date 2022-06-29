from unittest import TestCase

from parameterized import parameterized  # type: ignore

from pytezos.crypto.encoding import base58_decode
from pytezos.crypto.encoding import base58_encode
from pytezos.crypto.encoding import is_bh
from pytezos.crypto.encoding import is_l2_pkh
from pytezos.crypto.encoding import is_pkh
from pytezos.crypto.encoding import is_sig
from pytezos.crypto.encoding import scrub_input


class TestEncoding(TestCase):
    @parameterized.expand(
        [
            (b'NetXdQprcVkpaWU', b'Net'),
            (b'BKjWN8ALguCJ3oAjzMjZCNcFfUf1p9BfVAwYiVHs1QW3yMB9RNb', b'B'),
            (b'oop1fbAVi2ZwEt3vpu4uKpYGbbxumyMBSWwWf9qbByeM4JYAu92', b'o'),
            (b'LLoabcny4pVg1k6x3AktnNhwe1KSVBZh5Di45JeZPhUCmCu5Xj6ND', b'LLo'),
            (b'PtCJ7pwoxe8JasnHY8YonnLYjcVHmhiARPJvqcC6VfHT5s8k8sY', b'P'),
            (b'CoUeRwFZbV7NaAYRTz6n4ZLUkwiWcm7oKYdKCGcsEYHgVxSQxa4h', b'Co'),
            (b'tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq', b'tz1'),
            (b'tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu', b'tz2'),
            (b'tz3agP9LGe2cXmKQyYn6T68BHKjjktDbbSWX', b'tz3'),
            (b'txr1YNMEtkj5Vkqsbdmt7xaxBTMRZjzS96UAi', b'txr1'),
            (b'edpku976gpuAD2bXyx1XGraeKuCo1gUZ3LAJcHM12W1ecxZwoiu22R', b'edpk'),
            (b'sppk7aMNM3xh14haqEyaxNjSt7hXanCDyoWtRcxF8wbtya859ak6yZT', b'sppk'),
            (b'p2pk679D18uQNkdjpRxuBXL5CqcDKTKzsiXVtc9oCUT6xb82zQmgUks', b'p2pk'),
            (b'edsk3nM41ygNfSxVU4w1uAW3G9EnTQEB5rjojeZedLTGmiGRcierVv', b'edsk'),
            (b'spsk1zkqrmst1yg2c4xi3crWcZPqgdc9KtPtb9SAZWYHAdiQzdHy7j', b'spsk'),
            (b'p2sk3PM77YMR99AvD3fSSxeLChMdiQ6kkEzqoPuSwQqhPsh29irGLC', b'p2sk'),
            (b'edesk1zxaPJkhNGSzgZDDSphvPzSNrnbmqes8xzUrw1wdFxdRT7ePiQz8D2Q18fMjn6fC9ZRS2rUbg8d8snxxznE', b'edesk'),
            (b'spesk21cruoqtYmxfq5fpkXiZZRLRw4vh7VFJauGCAgHxZf3q6Q5LTv9m9dnMxyVjna6RzWQL45q4ppGLh97xZpV', b'spesk'),
            (b'p2esk1rqdHRPz4xQh8uP8JaWSVnGFTKxkh2utdjK5CPDTXAzzh5sXnnobLkGrXEZzGhCKFDSjv8Ggrjt7PnobRzs', b'p2esk'),
            (
                b'edsigtzLBGCyadERX1QsYHKpwnxSxEYQeGLnJGsSkHEsyY8vB5GcNdnvzUZDdFevJK7YZQ2ujwVjvQZn62ahCEcy74AwtbA8HuN',
                b'edsig',
            ),
            (
                b'spsig1RriZtYADyRhyNoQMa6AiPuJJ7AUDcrxWZfgqexzgANqMv4nXs6qsXDoXcoChBgmCcn2t7Y3EkJaVRuAmNh2cDDxWTdmsz',
                b'spsig',
            ),
            (
                b'sigUdRdXYCXW14xqT8mFTMkX4wSmDMBmcW1Vuz1vanGWqYTmuBodueUHGPUsbxgn73AroNwpEBHwPdhXUswzmvCzquiqtcHC',
                b'sig',
            ),
        ]
    )
    def test_b58_decode_encode(self, string, prefix):
        data = base58_decode(string)
        result = base58_encode(data, prefix)
        self.assertEqual(string, result)

    @parameterized.expand(
        [
            ('test', b'test'),
            (b'test', b'test'),
            ('0x74657374', b'test'),
        ]
    )
    def test_scrub_input(self, input_data, expected):
        self.assertEqual(expected, scrub_input(input_data))

    @parameterized.expand(
        [
            ('tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq', True),
            ('tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu', True),
            ('tz3agP9LGe2cXmKQyYn6T68BHKjjktDbbSWX', True),
            ('txr1YNMEtkj5Vkqsbdmt7xaxBTMRZjzS96UAi', False),
            ('KT1ExvG3EjTrvDcAU7EqLNb77agPa5u6KvnY', False),
            ('qwerty', False),
            ('tz1eKkWU5hGtfLUiq', False),
        ]
    )
    def test_is_pkh(self, value, expected):
        self.assertEqual(expected, is_pkh(value))

    @parameterized.expand(
        [
            ('tz1eKkWU5hGtfLUiqNpucHrXymm83z3DG9Sq', False),
            ('tz28YZoayJjVz2bRgGeVjxE8NonMiJ3r2Wdu', False),
            ('tz3agP9LGe2cXmKQyYn6T68BHKjjktDbbSWX', False),
            ('txr1YNMEtkj5Vkqsbdmt7xaxBTMRZjzS96UAi', True),
            ('KT1ExvG3EjTrvDcAU7EqLNb77agPa5u6KvnY', False),
            ('qwerty', False),
            ('tz1eKkWU5hGtfLUiq', False),
        ]
    )
    def test_is_l2_pkh(self, value, expected):
        self.assertEqual(expected, is_l2_pkh(value))

    @parameterized.expand(
        [
            (
                'edsigtzLBGCyadERX1QsYHKpwnxSxEYQeGLnJGsSkHEsyY8vB5GcNdnvzUZDdFevJK7YZQ2ujwVjvQZn62ahCEcy74AwtbA8HuN',
                True,
            ),
            (
                'spsig1RriZtYADyRhyNoQMa6AiPuJJ7AUDcrxWZfgqexzgANqMv4nXs6qsXDoXcoChBgmCcn2t7Y3EkJaVRuAmNh2cDDxWTdmsz',
                True,
            ),
            ('sigUdRdXYCXW14xqT8mFTMkX4wSmDMBmcW1Vuz1vanGWqYTmuBodueUHGPUsbxgn73AroNwpEBHwPdhXUswzmvCzquiqtcHC', True),
            ('qwerty', False),
            ('sigUdRdXYCXW14xqT8mFTMkX4wSmDMBmcW1Vuz1vanGWqYT', False),
        ]
    )
    def test_is_sig(self, value, expected):
        self.assertEqual(expected, is_sig(value))

    @parameterized.expand(
        [
            ('BLrbVv8rUfkpDZZ6efByhgjyDgPUFeKAfTMq8mWPmjXb9c5m8LJ', True),
            ('qwerty', False),
        ]
    )
    def test_is_bh(self, value, expected):
        self.assertEqual(expected, is_bh(value))
