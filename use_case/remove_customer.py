from abc import ABC, abstractmethod

class IRemoveCustomer(ABC):
    @abstractmethod
    def execute(self, request):
        """
        - takes a 'request' dict containing a customer 'id'
        - returns a 'response' dict containing the data from removed customer or a response dict with a 'error_msg' attribute informing that
          a customer hasn't been found
        """
        pass

class RemoveCustomer(IRemoveCustomer):
    def __init__(self, customer_gateway):
        self.customer_gateway = customer_gateway

    def execute(self, request):
        id = request['id']
        customer = self.customer_gateway.remove_customer(id)
        if customer == None:
            return {
                'error_msg': 'Unable to find a customer with id ' + id
            }
        else:
            return {
                'customer': response_from_entity(customer)
            }

def response_from_entity(customer_entity):
    from entity import customer
    return customer.customer_to_dict(customer_entity)
