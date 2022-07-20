# -*- coding: utf-8 -*-
"""
This module is used to define APP unique behavior
"""


def schema_deal_rule(page_name, schema_url):
    """
    Custom android schema jump rules

    > NOTE:  The schema jump rules within each app are inconsistent.

    The following is a simple example of a schema jump rule:

    assumptions:
     1.The jump rule inside the app is：
          schema_url = "trip://myUrl?url={}+type={}".format(schema_url, schema_type)
     2. The schema_url item has been configured in schema_url.json,
      such as: {"Home": "https://www.ctrip.com/"}

     ```py

         schema_type = 1

        # special processing according to keywords in schema_url
        keyword = 'rn_flight'
        if keyword in schema_url:
            schema_type = 1
            # Add your logic processing, for example： concatenate a pkg_id
             parameter to schema_url
            pkg_id = 123456
            schema_url = schema_url + "&pkgBuildId=" + str(pkg_id)
        # Handle schema_url of 'http://' or 'https'
        elif ('http://' in schema_url) or 'https' in schema_url:
            schema_type = 2
        elif '/index.html' in schema_url:
            schema_type = 3
        print('current schema:{}'.format(schema_url))
        schema_url = base64.b64encode(schema_url.encode('utf-8')).decode('utf-8')
        # the address that the app needs to jump to in the end
        schema_url = "trip://myUrl?url={}+type={}".format(schema_url, schema_type)
        return schema_url

    ```
    Parameters
        ----------
        page_name :
            The key of the schema_url to be jumped to
        schema_url : The value of the schema_url to be jumped to
    Returns
        -------
        schema_url string
    """
    return schema_url


def to_home():
    pass


def login(user_name, password):
    pass


def logout():
    pass


def get_mock_case_body(mock_case_id):
    """
    custom get mockCase response body

    :param mock_case_id: unique key for get mock data
    """
    mock_case_body = None
    # here add something to get mockCase response body...
    return mock_case_body


def create_browser_context(browser):
    """
    custom creates a new browser context.

    For related api, also see: https://playwright.dev/python/docs/api/class-browser#browser-new-context

    :param browser: the browser instance
    """
    context = None
    # here add something to create BrowserContext...
    #
    # For example, adding parameters when create,
    #   locale: language, viewport: screen size
    #
    # context = browser.new_context(record_video_dir="videos",
    #                               ignore_https_errors=True,
    #                               locale="en",
    #                               viewport={"width": 800, "height": 800})
    return context


def get_page_url(param):
    """
    Custom web get page url rules

    ```py
    # example 1
    import os
    from flybirds.utils import file_helper

    path = os.path.join(os.getcwd(), "config", "schema_url.json")
    if os.path.exists(path):
        c_f = file_helper.get_json_from_file(path)
        if c_f.__contains__(param):
                return c_f.get(param)

    # example 2
    url = "https://www.ctrip.com/"
    return url
    ```
    Parameters
        ----------
        param :
            The key of the schema_url to be jumped to in schema_url.config
    Returns
        -------
        url string
    """
    pass


def get_global_value(v):
    """
    replace with global cache
    """
    pass
