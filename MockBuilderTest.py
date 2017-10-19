import unittest
import MockBuilder


class RequestDataTest(unittest.TestCase):
    # @unittest.skip
    def testRequest(self):
        line = 'ID: 1#Address: http://172.16.72.143:9080/consultationIbs/CustomerConsultationWsService#Encoding: UTF-8#Http-Method: POST#Content-Type: text/xml#Headers: {Accept=[*/*], SOAPAction=["http://bancointernacional.com.ec/wsdl/consultation/customer/CustomerConsultationImpl/ibsGetCustomerProductsRequest"]}#Payload: <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:ibsGetCustomerProducts xmlns:ns2="http://bancointernacional.com.ec/wsdl/consultation/customer"><arg0><ipAddress>192.168.2.31</ipAddress><channel>WEB</channel><customerId>000000364</customerId><additionalCusId></additionalCusId><sequential>6167005</sequential><dateAndTime>2017-09-27 12:01:23.118</dateAndTime><userId>CANOMNIA</userId><productCode>1</productCode><serviceCode>10003</serviceCode><tranServiceCode>1111</tranServiceCode><groupId>G9</groupId><bankId>01</bankId></arg0></ns2:ibsGetCustomerProducts></soap:Body></soap:Envelope>#'
        soap = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:ibsGetCustomerProducts xmlns:ns2="http://bancointernacional.com.ec/wsdl/consultation/customer"><arg0><ipAddress>192.168.2.31</ipAddress><channel>WEB</channel><customerId>000000364</customerId><additionalCusId></additionalCusId><sequential>6167005</sequential><dateAndTime>2017-09-27 12:01:23.118</dateAndTime><userId>CANOMNIA</userId><productCode>1</productCode><serviceCode>10003</serviceCode><tranServiceCode>1111</tranServiceCode><groupId>G9</groupId><bankId>01</bankId></arg0></ns2:ibsGetCustomerProducts></soap:Body></soap:Envelope>'
        mb = MockBuilder.MockBuilder()
        data = mb.get_request_data(line)
        post = data['method']
        url = data['url']
        body_patterns = data['bodyPatterns']
        # body = [{'equalTo': soap}]
        # print(body_patterns)
        # print(soap)

        self.assertEqual('/consultationIbs/CustomerConsultationWsService', url)
        self.assertEqual('POST', post)
        self.assertEqual(soap, body_patterns)

    # @unittest.skip
    def testResponse(self):
        line = 'ID: 4#Response-Code: 200#Encoding: UTF-8#Content-Type: text/xml; charset=UTF-8#Headers: {Content-Language=[en-US], Content-Length=[513], content-type=[text/xml; charset=UTF-8], Date=[Wed, 27 Sep 2017 17:12:03 GMT], X-Powered-By=[Servlet/3.0]}#Payload: <?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><dlwmin:ibsGetCustomerProductsResponse xmlns:dlwmin="http://bancointernacional.com.ec/wsdl/consultation/customer" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><CustomerProductResponse><messageDescr>OK</messageDescr><messageId>0</messageId><products>005|002|001|004|</products></CustomerProductResponse></dlwmin:ibsGetCustomerProductsResponse></soapenv:Body></soapenv:Envelope>#'
        mb = MockBuilder.MockBuilder()
        data = mb.get_response_data(line)
        status = data['status']
        headers = data['headers']
        content_len = headers['Content-Length']
        response_body = data['response_body']

        self.assertEqual(200, status)
        self.assertEqual('513', content_len)
        self.assertTrue(str(response_body).startswith('<?xml version="1.0" encoding="UTF-8"?>'))
        self.assertTrue(str(response_body).endswith('</soapenv:Envelope>'))

    # def testDB(self):
    #     mb = MockBuilder.MockBuilder()
    #     mb.setup_db()
    #     self.assertTrue(True)

    # def testWirteFile(self):
    #     mb = MockBuilder.MockBuilder()
    #     mb.write_request_response_files()
    #     self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
