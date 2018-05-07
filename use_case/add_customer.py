from abc import ABC, abstractmethod

class IAddCustomer(ABC):
    @abstractmethod
    def execute(self, request):
        """
        - takes a 'request' which is a dictionary containing customer data to create a 'Customer' entity,
        - returns a 'response' dictionary containing an 'id' for the customer just added
        """
        pass

class AddCustomer(IAddCustomer):
    def __init__(self, customer_gateway):
        self.customer_gateway = customer_gateway

    def execute(self, request):
        customer = request_to_entity(request)
        id = self.customer_gateway.add_customer(customer)
        return {
            'id': id
        }

# HELPER FUNCTIONS

def request_to_entity(request):
    from entity import customer
    import uuid

    id = str(uuid.uuid4())
    name = request['name']
    address = request['address']
    return customer.CustomerEntity(id, name, address)
