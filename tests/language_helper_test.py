from unittest import TestCase
from unittest import main
from flybirds.utils import language_helper


class LanguageHelperTest(TestCase):
    """
    language helper test
    """

    def test_parse_keyword(self):
        k_w = language_helper.parse_keyword("when", "zh-CN")
        self.assertEqual(k_w, "当")

    def test_parse_glb_str(self):
        k_w = language_helper.parse_glb_str("rerun failed scenario", "en")
        self.assertEqual(k_w, "rerun failed scenario")

    def test_parse_glb_step(self):
        k_w = language_helper.parse_glb_step("start app", "en")
        self.assertEqual(k_w[0], "start app")

    def test_get_language_list(self):
        lg_list = language_helper.get_language_list()
        self.assertIn("en", lg_list)

    def test_parse_keyword_i18(self):
        g_step_name = language_helper.parse_glb_str(
            "information association of failed"
            " operation",
            "zh-CN",
        )
        then_key = language_helper.parse_keyword(
            "then",  "zh-CN",
        )
        f_d = f"{then_key} {g_step_name}\n"
        l_f_d = f_d.format(3, "4234234")
        self.assertIn("那么", l_f_d)


if __name__ == "__main__":
    main()
