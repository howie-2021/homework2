import requests

resp = requests.head('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789')
assert(resp.status_code == 200)
print(resp.status_code)

resp = requests.head('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1')
assert(resp.status_code == 403)
print(resp.status_code)