import unittest
import roman

class ToArabicTest(unittest.TestCase):
    simpleValues = [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ]

    def testSimpleValuesRomans(self):
        for c in ToArabicTest.simpleValues:
            self.assertEqual(roman.Roman(c[0]).toArabic(), c[1])

    def testBigger(self):
        cases = [
            ("VI", 6),
            ("XI", 11),
            ("LI", 51),
            ("CI", 101),
            ("DI", 501),
            ("MI", 1001)
        ]
        for c in cases:
            self.assertEqual(roman.Roman(c[0]).toArabic(), c[1])

    def testSmaller(self):
        cases = [
            ("IV", 4),
            ("IX", 9),
            ("IL", 49),
            ("IC", 99),
            ("ID", 499),
            ("IM", 999),
            ("XIV", 14),
            ("XIIV", 13)
        ]
        for c in cases:
            self.assertEqual(roman.Roman(c[0]).toArabic(), c[1], c[0])

if __name__ == "__main__":
    unittest.main()
