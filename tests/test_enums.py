import json
import unittest

from inttegro.otp import Purpose as OTPPurpose
from inttegro.product import Type as ProductType
from inttegro.refund import Reason as RefundReason
from inttegro.upload_request import Status as UploadRequestStatus


class ApiEnumTest(unittest.TestCase):
    def test_wire_enums_are_public_and_json_compatible(self):
        encoded = json.dumps(
            {
                "product": ProductType.DIGITAL,
                "otp": OTPPurpose.SIGN_IN,
                "refund": RefundReason.REQUESTED_BY_CUSTOMER,
                "status": UploadRequestStatus.PENDING,
            }
        )
        self.assertEqual(
            encoded,
            '{"product": "digital", "otp": "sign_in", "refund": "requested_by_customer", "status": "pending"}',
        )


if __name__ == "__main__":
    unittest.main()
