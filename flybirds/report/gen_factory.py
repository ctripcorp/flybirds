# -*- coding: utf-8 -*-
"""
report gen factory
"""
from flybirds.utils import flybirds_log as log


class GenFactory:
    """
    gen factory
    """
    gen_factories = {}

    @staticmethod
    def gen(gen_type, report_path):
        """
        auto gen
        """
        if gen_type is not None and GenFactory.gen_factories.__contains__(
                gen_type):

            GenFactory.gen_factories[gen_type].gen(report_path)
        else:
            log.info("not have this kind of report type")

    @classmethod
    def add(cls, gen_obj):
        """
        add report gen
        """
        if hasattr(gen_obj, "name"):
            cls.gen_factories[gen_obj.name] = gen_obj
