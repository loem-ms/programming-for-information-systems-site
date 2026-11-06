import unittest
from policy import pickup_label


class PolicyTests(unittest.TestCase):
    @unittest.skip("Replace with an independently expected reviewed-boundary case")
    def test_reviewed_boundary(self):
        self.fail("Write an expected result before implementing the policy")

    @unittest.skip("Replace with an independently expected unreviewed case")
    def test_unreviewed_request(self):
        self.fail("Specify what unreviewed means before implementing the policy")


if __name__ == "__main__":
    unittest.main()
