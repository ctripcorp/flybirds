# -*- coding: utf-8 -*-
import unittest
import flybird.utils.flybird_log as log


class TestlogMethods(unittest.TestCase):
    def test_logdebug(self):
        with self.assertLogs("flybird_log", level="DEBUG") as cm:
            log.debug("this is test1")
            log.debug("this is test2", "this is test3")

            self.assertEqual(
                [
                    "DEBUG:flybird_log:this is test1",
                    "DEBUG:flybird_log:this is test2",
                    "DEBUG:flybird_log:this is test3",
                ],
                cm.output,
            )

    def test_loginfo(self):
        with self.assertLogs("flybird_log", level="INFO") as cm:
            log.info("this is test1")
            log.info("this is test2", "this is test3")

            self.assertEqual(
                [
                    "INFO:flybird_log:this is test1",
                    "INFO:flybird_log:this is test2",
                    "INFO:flybird_log:this is test3",
                ],
                cm.output,
            )

    def test_logwarn(self):
        with self.assertLogs("flybird_log", level="WARN") as cm:
            log.warn("this is test1")
            log.warn("this is test2", "this is test3")

            self.assertEqual(
                [
                    "WARNING:flybird_log:this is test1",
                    "WARNING:flybird_log:this is test2",
                    "WARNING:flybird_log:this is test3",
                ],
                cm.output,
            )

    def test_logerror(self):
        with self.assertLogs("flybird_log", level="ERROR") as cm:
            log.error("this is test1")
            log.error("this is test2", "this is test3")

            self.assertEqual(
                [
                    "ERROR:flybird_log:this is test1",
                    "ERROR:flybird_log:this is test2",
                    "ERROR:flybird_log:this is test3",
                ],
                cm.output,
            )


if __name__ == "__main__":
    unittest.main()
