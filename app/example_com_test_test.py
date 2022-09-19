# NOTE: Generated By HttpRunner v4.2.0
# FROM: example.com_test.json
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseExampleComTest(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("")
            .get("http://example.com/")
            .with_headers(
                **{
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Host": "example.com",
                    "If-Modified-Since": "Thu, 17 Oct 2019 07:18:26 GMT",
                    "If-None-Match": '"3147526947+ident"',
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 200, "assert response status code")
            .assert_equal(
                'headers."Content-Type"',
                "text/html; charset=UTF-8",
                "assert response header Content-Type",
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseExampleComTest().test_start()
