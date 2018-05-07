from use_case import add_customer, retrieve_customers, remove_customer
from gateway import customer_gateway

database_file = 'customers.db'

gateway = customer_gateway.InMemoryCustomerGateway(database_file)

def ask_option():
    print('1 - List customers')
    print('2 - Add customer')
    print('3 - Remove customer')
    print('0 - Quit')
    return int(input('Choose an option: '))

def add_customer_interaction():
    uc = add_customer.AddCustomer(gateway)

    name = input('Customer name: ')
    address = input('Customer address: ')

    request = {'name': name, 'address': address}

    response = uc.execute(request)

    print('User ' + response['id'] + ' added successfully')

def retrieve_customers_interaction():
    uc = retrieve_customers.RetrieveAllCustomers(gateway)

    response = uc.execute()

    counter = 1
    for customer in response['customers']:
        print('[' + str(counter) + '] - ' + str(customer))
        counter += 1

def remove_customer_interaction():
    retrieve_customers_uc = retrieve_customers.RetrieveAllCustomers(gateway)
    remove_customer_uc = remove_customer.RemoveCustomer(gateway)

    retrieve_response = retrieve_customers_uc.execute()
    customers = retrieve_response['customers']
    index_input = int(input('Enter customer index: '))
    index = index_input - 1
    if 0 <= index <= len(customers):
        remove_response = remove_customer_uc.execute({'id': customers[index]['id']})
        if 'customer' in remove_response:
            print('Customer ' + str(remove_response['customer']) + ' removed successfully')
        else:
            print('Error: ' + remove_response['error_msg'])
    else:
        print('Index ' + str(index_input) + ' is out of bounds')

def main():
    print('WELCOME TO CUSTOMER MANAGEMENT')

    while True:
        op = ask_option()

        if op == 1:
            retrieve_customers_interaction()
        elif op == 2:
            add_customer_interaction()
        elif op == 3:
            remove_customer_interaction()
        elif op == 0:
            exit(0)
        else:
            print('Invalid option: ' + str(op))

main()
