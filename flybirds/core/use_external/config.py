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
