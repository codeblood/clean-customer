class CustomerEntity:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return 'id:' + self.id + ' ,name:' + self.name + ' ,address:' + self.address

def customer_from_dict(dictionary):
    return CustomerEntity(dictionary['id'], dictionary['name'], dictionary['address'])

def customer_to_dict(customer):
    return vars(customer)
