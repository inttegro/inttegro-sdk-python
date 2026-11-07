import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro import order, request


class RequestMetadataTest(unittest.TestCase):
    def test_serializes_response_projection(self) -> None:
        metadata = order.CreateNewCustomerInputRequestMeta(
            response=request.Response(
                projection={
                    "order": request.Pick(
                        pick=("id", "status", "customer.name")
                    ),
                    "payment": request.Omit(omit=("latest_error",)),
                }
            )
        )

        self.assertEqual(
            {
                "response": {
                    "projection": {
                        "order": {
                            "pick": ["id", "status", "customer.name"]
                        },
                        "payment": {"omit": ["latest_error"]},
                    }
                }
            },
            metadata.to_dict(),
        )

    def test_rejects_empty_property_selection(self) -> None:
        with self.assertRaises(ValueError):
            request.Pick(pick=())


if __name__ == "__main__":
    unittest.main()
