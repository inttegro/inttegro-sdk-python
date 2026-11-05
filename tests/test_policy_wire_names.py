import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inttegro.children_policy import BTAgingSpec as ChildrenPolicyBTAgingSpec
from inttegro.operating_policy import BTAgingSpec as OperatingPolicyBTAgingSpec


class PolicyWireNamesTest(unittest.TestCase):
    def test_aging_specs_expose_public_id(self) -> None:
        children = ChildrenPolicyBTAgingSpec.from_dict(
            {"public_id": "bt_aging_spec_immediate", "t_plus": "0h"}
        )
        operating = OperatingPolicyBTAgingSpec.from_dict(
            {"public_id": "bt_aging_spec_168_hourly", "t_plus": "168h"}
        )

        self.assertEqual("bt_aging_spec_immediate", children.public_id)
        self.assertEqual("bt_aging_spec_168_hourly", operating.public_id)
        self.assertEqual(
            {"public_id": "bt_aging_spec_168_hourly", "t_plus": "168h"},
            operating.to_dict(),
        )


if __name__ == "__main__":
    unittest.main()
