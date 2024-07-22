"""Model Registry REST API.

REST API for Model Registry to create and manage ML model metadata

The version of the OpenAPI document: v1alpha3
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from mr_openapi.models.inference_service_update import InferenceServiceUpdate


class TestInferenceServiceUpdate(unittest.TestCase):
    """InferenceServiceUpdate unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InferenceServiceUpdate:
        """Test InferenceServiceUpdate
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `InferenceServiceUpdate`
        """
        model = InferenceServiceUpdate()
        if include_optional:
            return InferenceServiceUpdate(
                custom_properties = {
                    'key' : null
                    },
                description = '',
                external_id = '',
                model_version_id = '',
                runtime = '',
                desired_state = 'DEPLOYED'
            )
        else:
            return InferenceServiceUpdate(
        )
        """

    def testInferenceServiceUpdate(self):
        """Test InferenceServiceUpdate."""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()