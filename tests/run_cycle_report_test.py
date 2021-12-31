from unittest import TestCase
from unittest import main
from flybird.core.launch_cycle.run_manage import RunManage


class Report(TestCase):
    def test_report(self):
        self.assertEqual(len(RunManage.after_run_processor),
                         1)


if __name__ == "__main__":
    main()
