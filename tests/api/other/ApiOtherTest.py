from tests.api.ApiBaseTest import ApiBaseTest


class ApiOtherTest(ApiBaseTest):
    def test_healthz(self):
        # given
        expected_response = {"status": "ok"}

        # when
        response = self.test_api.get(
            url="/healthz",
        )
        response_json = response.json()

        # then
        assert response_json == expected_response

    def test_call_endpoint_with_wrong_auth_token(self):
        # given
        token = 'wrong_token'
        payload = {}

        # when
        response = self.test_api.post(
            url="/geo/reverse",
            json=payload,
            headers={'X-API-KEY': token}
        )

        # then
        assert response.status_code == 401
