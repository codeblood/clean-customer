from abc import ABC, abstractmethod

class IRetrieveAllCustomers(ABC):
    @abstractmethod
    def execute(self):
        """
        - takes no arguments
        - returns a response dictionary containing a list of all customers registered
        """
        pass

class RetrieveAllCustomers(IRetrieveAllCustomers):
    def __init__(self, customer_gateway):
        self.customer_gateway = customer_gateway

    def execute(self):
        customers = self.customer_gateway.retrieve_all_customers()
        return {
            'customers': list(map(response_from_entity, customers))
        }

# HELPER FUNCTIONS

def response_from_entity(customer_entity):
    from entity import customer
    return customer.customer_to_dict(customer_entity)
