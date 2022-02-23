# -*- coding: utf-8 -*-
"""
This module is used to define APP unique behavior
"""


def schema_deal_rule(page_name, schema_url):
    """
    Custom schema jump rules

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
