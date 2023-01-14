"""# (1) Returns all customers from customer table
customers = Customers.objects.all()

# (2)Returns first customer in table
firstCustomer =Customers.objects.first()

# (3)Returns last customer in table 
lastCustomer = Customer.object.last()

# (4)Returns single customer by name 
customerByname = Customer.object.get(name='Ajmal')

# (5)Returns single customer by name 
customerById = Customer.object.get(id=4)

# (6)Returns all orders related to customer (firstCustomer cariable set above)
firstCustomer.order._set.all()

# (7)Returns order customer name:(Query parent model values)
order = Order.objects.first()
parentName = order.customer.name 

# (8)Returns products from products table with catogory "Out Door" in category atribute
products = Product.objects.filter(category='Out Door')

# (9)Order/sort Objects by id 
leastToGreatest = Product.object.all().order_by('id')
greateToLeast = Products.object.all().order_by('-id)

#(10)Returns all products with tag og "Sports": (Quary Many to Many Fields)
productsFiltered = Products.objects.filter(tags__name="Sports)

"""


