from .base import BasePayantAPI


class Invoice(BasePayantAPI):

    def __init__(self, auth_key):
        super(Invoice, self).__init__(auth_key)
        self.base_invoice_key = "invoices"

    def add(self, new=False, **kwargs):
        """

        Create a new invoice
        :param client_id: Client ID
        :param due_date:  Invoice due date
        :param fee_bearer: Invoice fee bearer account or client
        :param items: Invoice items
        :param new: False by default but True if the client is new
        :param client: Client Data
        :return:
        """
        due_date = kwargs.get('due_date')
        fee_bearer = kwargs.get('fee_bearer')
        client_id = kwargs.get('client_id')
        items = kwargs.get('items')
        url = self._path(self.base_invoice_key)

        if new:
            request_data = {
                "client": kwargs.get('client'),
                "due_date": due_date,
                "fee_bearer": fee_bearer,
                "items": items,
            }
        else:
            request_data = {
                "client_id": client_id,
                "due_date": due_date,
                "fee_bearer": fee_bearer,
                "items": items
            }
        # import ipdb
        # ipdb.set_trace()
        new_data = self._exec_request('POST', url, request_data)
        return new_data

    def get(self, reference_code):
        """
        Get the details of an invoice with the reference_code provided.
        :param reference_code:
        :return:
        """
        url = self._path("{0}/{1}".format(self.base_invoice_key,
                                          reference_code))
        return self._exec_request('GET', url)

    def send(self, reference_code):
        """
        Send an invoice
        :param reference_code:
        :return:
        """
        _send_base = "send"
        url = self._path("{0}/{1}/{2}".format(self.base_invoice_key,
                                              _send_base, reference_code))
        return self._exec_request('GET', url)

    def history(self, period, start, end):
        """
        Return invoice history from start to end within specified period
        :param period:
        :param start:
        :param end:
        :return:
        """
        _history_base = "history"
        url = self._path("{0}/{1}/".format(self.base_invoice_key,
                                           _history_base))
        request_data = {"period": period, "start": start, "end": end}
        return self._exec_request('GET', url, request_data)

    def delete(self, reference_code):
        url = self._path("{0}/{1}".format(self.base_invoice_key,
                                          reference_code))
        return self._exec_request('DELETE', url)


items = {
    "name": "Website Design",
    "description": "5 Pages Website plus 1 Year Web Hosting",
    "unit_cost": "50000.00",
    "quantity": "1"
}

test_user = {
    "company_name": "Albert Specialist Hospital",
    "first_name": "Albert",
    "last_name": "Jane",
    "email": "jane@alberthospital.com",
    "phone": "+2348012345678",
    "website": "http://www.alberthospital.com",
    "address": "Wase II",
    "state": "37",
    "lga": "782"
}
#
# test = Invoice(auth_key="2af20ba3197ee1108fa27844ea20b6e9472612a9d0bdadadf30c7bf3")
# # print test.add(client=test_user, due_date="12/30/2016", fee_bearer="client", items=items, new=True)
# test.add(due_date="12/30/2016", fee_bearer="client", items="", new=False)
