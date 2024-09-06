import flybirds.core.global_resource as gr


class Config:
    """
    config
    """

    @staticmethod
    def get_config():
        """
        get config
        """
        return gr.get_value("configManage", None)

    @staticmethod
    def get_ele_locator():
        """
        get ele locator
        """
        config = Config.get_config()
        if config is not None:
            return config.ele_locator_info

    @staticmethod
    def get_app_info():
        """
        get app info
        """
        config = Config.get_config()
        if config is not None:
            return config.app_info

    @staticmethod
    def get_platform():
        """
        get platform info
        """
        return gr.get_platform()

    @staticmethod
    def get_device_instance():
        """
        get driver
        """
        return gr.get_value("deviceInstance", None)

    @staticmethod
    def get_poco_instance():
        """
        get poco
        """
        return gr.get_value("pocoInstance", None)

    @staticmethod
    def get_ocr_instance():
        """
        get ocr
        """
        return gr.get_value("ocrInstance", None)

    @staticmethod
    def get_rerun_fail_info():
        """
        get app env config
        """
        return gr.get_value("appEnvConfig", None)

    @staticmethod
    def get_package_name():
        """
        get package name
        """
        return gr.get_value("packageName", None)

    @staticmethod
    def get_device_id():
        """
        get device id
        """
        return gr.get_value("deviceid", None)

    @staticmethod
    def get_web_driver_agent():
        """
        get web driver agent
        """
        return gr.get_value("web_driver_agent", None)

    @staticmethod
    def get_playwright():
        """
        get playwright
        """
        return gr.get_value("playwright", None)

    @staticmethod
    def get_browser():
        """
        get browser
        """
        return gr.get_value("browser", None)

    @staticmethod
    def get_plugin_page():
        """
        get plugin page
        """
        return gr.get_value("plugin_page", None)

    @staticmethod
    def get_browser_context():
        """
        get browser context
        """
        return gr.get_value("browser_context", None)
