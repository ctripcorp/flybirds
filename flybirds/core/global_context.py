# -*- coding: utf-8 -*-
"""
global plugin holder
"""
import operator
from threading import local

from flybirds.core.plugin.plugin_proxy import PluginProxy


class GlobalContext:
    """
    global plugin context, init on behave hook event
    """

    def __init__(self):
        pass

    device = PluginProxy()
    page = PluginProxy()
    element = PluginProxy()
    app = PluginProxy()
    step = PluginProxy()
    screen = PluginProxy()
    screen_record = PluginProxy()
    ui_driver = PluginProxy()
    interception = PluginProxy()
    platform = None
    config = None
    config_processor = []
    before_run_processor = []
    after_run_processor = []
    before_feature_processor = []
    after_feature_processor = []
    before_scenario_processor = []
    after_scenario_processor = []
    before_step_processor = []
    after_step_processor = []
    before_ui_driver_processor = []
    after_ui_driver_processor = []
    before_tag_processor = []
    after_tag_processor = []
    plugin_processor = []
    language = "zh-CN"
    device_driver = None
    ui_driver_instance = None
    ocr_driver_instance = None
    active_plugin = "default"
    connector = None
    current_local = local()
    ocr_result = []
    struct_ocr_result = []
    ocr_regional_result = []
    image_size = []

    @classmethod
    def set_current_language(cls, l_g):
        cls.current_local.language = l_g

    @classmethod
    def get_current_language(cls):
        return cls.current_local.language

    @classmethod
    def del_current_language(cls):
        c_l = cls.current_local
        del c_l.language

    @classmethod
    def set_global_cache(cls, key, value):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            cls.current_local.glb_cache = {}
        cls.current_local.glb_cache[key] = value

    @classmethod
    def get_global_cache(cls, key):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            return None
        return cls.current_local.glb_cache.get(key)

    @classmethod
    def del_global_cache(cls):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            return None
        rc_l = cls.current_local
        del rc_l.glb_cache

    @staticmethod
    def process(processors_name, *args):
        """
        processor executor
        """
        processors = getattr(GlobalContext, processors_name)
        if processors is not None and len(processors) > 0:
            sort_key = operator.attrgetter("order")
            processors.sort(key=sort_key)
            for processor in processors:
                if hasattr(processor, "can"):
                    can_run = processor.can(*args)
                    if can_run is True:
                        processor.run(*args)
                else:
                    processor.run(*args)

    @staticmethod
    def join(processors_name, processor, replace=0):
        """
        add processor to plugin glob processor, where replace is 1 new
        processor will replace the older
        """
        indx = -1
        if processor is not None and processor.name is not None:
            processors = getattr(GlobalContext, processors_name)
            for i, item in enumerate(processors):
                if item.name is not None and item.name == processor.name:
                    indx = i
                    break
            if replace == 0:
                if indx >= 0:
                    return indx
            elif indx >= 0:
                processors[indx] = processor
                return indx
            processors.append(processor)

        return indx

    @staticmethod
    def insert(processors_name, processor, replace=0):
        """
        insert into processor at first one place and  will remove old one
        when the replace is 1
        """
        indx = -1
        if processor is not None and processor.name is not None:
            processors = getattr(GlobalContext, processors_name)
            for i, item in enumerate(processors):
                if item.name is not None and item.name == processor.name:
                    indx = i
                    break
            if replace == 0:
                if indx >= 0:
                    return indx
            elif indx >= 0:
                del processors[indx]
            processors.insert(0, processor)

        return indx
