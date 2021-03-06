from setuptools import setup

setup(
    name="opaque_keys",
    version="0.1.1",
    packages=[
        "opaque_keys",
        "opaque_keys.edx",
    ],
    install_requires=[
        "stevedore",
        "pymongo"
    ],
    entry_points={
        'opaque_keys.testing': [
            'base10 = opaque_keys.tests.test_opaque_keys:Base10Key',
            'hex = opaque_keys.tests.test_opaque_keys:HexKey',
            'dict = opaque_keys.tests.test_opaque_keys:DictKey',
        ],
        'course_key': [
            'course-v1 = opaque_keys.edx.locator:CourseLocator',
            # don't use slashes in any new code
            'slashes = opaque_keys.edx.locator:CourseLocator',
        ],
        'usage_key': [
            'block-v1 = opaque_keys.edx.locator:BlockUsageLocator',
            'location = opaque_keys.edx.locations:DeprecatedLocation',
        ],
        'asset_key': [
            'asset-v1 = opaque_keys.edx.locator:AssetLocator',
        ],
        'definition_key': [
            'def-v1 = opaque_keys.edx.locator:DefinitionLocator',
        ],
    }

)
