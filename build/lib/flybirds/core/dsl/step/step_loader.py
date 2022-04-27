# -*- coding: utf-8 -*-
"""
behave cannot get language from json report,use this to change the behave func
"""

import six
from behave.formatter.json import JSONFormatter
from behave.step_registry import StepRegistry
from flybirds.core.extend.step import load_steps

import flybirds.utils.flybirds_log as log
import flybirds.utils.language_helper as lge

# hold behave add step func
step_registry_add_step = StepRegistry.add_step_definition
language_list = lge.get_language_list()


# inject behave function: json format
def inject_behave():
    """
    change behave func
    """
    log.info("change behave json format feature to flybirds feature")
    JSONFormatter.feature = feature_wreap
    log.info(
        "change behave add_step_definition to flybirds add_step_definition"
    )
    if (StepRegistry.add_step_definition.__module__ == "behave.step_registry"
            or StepRegistry.add_step_definition.__name__
                    .find("add_step_definition") >= 0):
        StepRegistry.add_step_definition = step_registry_add_step_wreap


def feature_wreap(self, feature):
    """
    wreap behave feature
    """
    self.reset()
    self.current_feature = feature
    self.current_feature_data = {
        "keyword": feature.keyword,
        "name": feature.name,
        "tags": list(feature.tags),
        "location": six.text_type(feature.location),
        "status": None,  # Not known before feature run.
        "language": feature.language,
    }
    element = self.current_feature_data
    if feature.description:
        element["description"] = feature.description


def step_registry_add_step_wreap(self, keyword, step_text, func):
    """
    wreap behave add_step_definition
    """
    step_type = keyword.lower()

    if (
            step_type == "step"
            and language_list is not None
            and len(language_list) > 0
    ):
        for language_item in language_list:
            txt_list = lge.parse_glb_step(step_text, language_item)
            if txt_list is not None and len(txt_list) > 0:
                for txt in txt_list:
                    step_registry_add_step(self, keyword, txt, func)
    step_registry_add_step(self, keyword, step_text, func)


# start inject
inject_behave()

# load step
load_steps()
