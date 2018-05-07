from abc import ABC, abstractmethod

class CustomerGateway(ABC):
    @abstractmethod
    def add_customer(self, customer):
        """
        - takes an instance of entity.Customer
        - returns an 'id' for the added customer
        """
        pass

    @abstractmethod
    def retrieve_all_customers(self):
        """
        - takes no arguments
        - returns a list with all registered customers
        """
        pass

    @abstractmethod
    def remove_customer(self, id):
        """
        - takes a customer 'id' as argument
        - returns the customer entity just removed or None if a customer with the given 'id' wasn't found
        """
        pass

#    @abstractmethod
    def match_customer(self):
        """
        - takes a dictionary with customer fields
        - returns a customer entity list or None if no customer matching the dictionary field were found
        """
        pass


class InMemoryCustomerGateway(CustomerGateway):
    def __init__(self, file_path = ''):
        self.file_path = file_path
        if self.file_path != '':
            self.customers = load(self.file_path)
        else:
            self.file_path = './customers.db'
            self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        persist(self.file_path, self.customers)
        return customer.id

    def retrieve_all_customers(self):
        return self.customers

    def remove_customer(self, id):
        filtered = list(filter(lambda customer: customer.id == id, self.customers))
        if filtered == []:
            return None
        else:
            customer = filtered[0]
            self.customers.remove(customer)
            persist(self.file_path, self.customers)
            return customer

    def match_customer(self, dictionary):
        pass

# HELPER FUNCTIONS

def serialize_entity(customer):
    return str({
        'id': customer.id,
        'name': customer.name,
        'address': customer.address
    })


def deserialize_entity(string):
    import ast
    record = ast.literal_eval(string)

    from entity import customer
    return customer.CustomerEntity(
        id = record['id'],
        name = record['name'],
        address = record['address']
    )

def persist(file_path, customers):
    dump = ''
    for cust_string in map(serialize_entity, customers):
        dump += cust_string + '\n'
    f = open(file_path, 'w')
    f.write(dump)
    f.close()

def load(file_path):
    f = open(file_path, 'r')
    dump = f.read().strip()
    f.close()
    return list(map(deserialize_entity, dump.split('\n')))
