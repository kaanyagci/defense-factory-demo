import unittest
from app import get_document


class DocumentAccessTests(unittest.TestCase):
    def test_owner_can_read_own_document(self):
        self.assertEqual(get_document('alice', 'report-1')['body'], "Alice's planning notes")

    def test_user_cannot_read_someone_elses_document(self):
        self.assertIsNone(get_document('alice', 'report-2'))

    def test_missing_document_does_not_exist(self):
        self.assertIsNone(get_document('alice', 'missing'))

    def test_missing_identity_is_denied(self):
        self.assertIsNone(get_document(None, 'report-1'))


if __name__ == '__main__':
    unittest.main()
