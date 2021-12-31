# -*- coding: utf-8 -*-
import unittest
import flybirds.utils.flybirds_log as log


class TestlogMethods(unittest.TestCase):
    def test_logdebug(self):
        with self.assertLogs("flybirds_log", level="DEBUG") as cm:
            log.debug("this is test1")
            log.debug("this is test2", "this is test3")

            self.assertEqual(
                [
                    "DEBUG:flybirds_log:this is test1",
                    "DEBUG:flybirds_log:this is test2",
                    "DEBUG:flybirds_log:this is test3",
                ],
                cm.output,
            )

    def test_loginfo(self):
        with self.assertLogs("flybirds_log", level="INFO") as cm:
            log.info("this is test1")
            log.info("this is test2", "this is test3")

            self.assertEqual(
                [
                    "INFO:flybirds_log:this is test1",
                    "INFO:flybirds_log:this is test2",
                    "INFO:flybirds_log:this is test3",
                ],
                cm.output,
            )

    def test_logwarn(self):
        with self.assertLogs("flybirds_log", level="WARN") as cm:
            log.warn("this is test1")
            log.warn("this is test2", "this is test3")

            self.assertEqual(
                [
                    "WARNING:flybirds_log:this is test1",
                    "WARNING:flybirds_log:this is test2",
                    "WARNING:flybirds_log:this is test3",
                ],
                cm.output,
            )

    def test_logerror(self):
        with self.assertLogs("flybirds_log", level="ERROR") as cm:
            log.error("this is test1")
            log.error("this is test2", "this is test3")

            self.assertEqual(
                [
                    "ERROR:flybirds_log:this is test1",
                    "ERROR:flybirds_log:this is test2",
                    "ERROR:flybirds_log:this is test3",
                ],
                cm.output,
            )


if __name__ == "__main__":
    unittest.main()
