# Page element
In front-end software (IOS, Android, H5), a button is an element, a text box is an element, a card, and a list are also elements on this page. The relationship between elements is a tree, which may be juxtaposed or contained.

We can understand front-end software testing as follows:

In the limited data environment, interact with some page elements to verify whether the other page elements meet the requirements and expected performance.

The limited data environment can be realized through mock service message. Elements can respond to finger clicks and instructions transmitted by the operating system. The remaining points that we need to pay attention to are the identification of elements and whether elements meet the expected performance.

In manual testing, the identification of elements is judged by the human eye for the location, color, copy and other characteristics of elements.

In the UI automation test platform, an element has attributes such as location (XPath), copy, ID, accessibility label, etc. a short and unique attribute is suitable for identifying elements. Copywriting and accessibility labels are recommended.

To judge whether the element meets the expected performance, it depends on the specific situation: to judge whether the copy meets the expectation, compare the element copy with the expected value; Judge whether the element is displayed in the second item of the list, fix the accessibility label of the second item of the list, and identify whether it is the target attribute by obtaining other attributes of the second item.

Frankly speaking, there must be cases that only manual testing can not be verified by automated testing, but if most of the cases can use automated testing, we can also alleviate the problems we are facing and benefit from it.

# How to inspect Page element
**Mobile**
1.  Install IDE editor officially provided by airtest：[Download](https://airtest.netease.com/) 
2.  [IDE manual](https://airtest.doc.io.netease.com/IDEdocs/3.1getting_started/AirtestIDE_install/)

**Web**
1. Element selector：[Selectors](https://playwright.dev/python/docs/selectors)
