class Product:
    def __init__(self,name,price,discountPercent):
        self.name=name
        self.price=price
        self.discountPercent=discountPercent

    def getDiscountAmount(self):
        return self.price*self.discountPercent/100
    
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

def show_product_list(products):
    print "PRODUCTS"
    for i in range(len(products)):
        p=products[i]
        print str(i+1)+". "+p.name
    print

def show_products(product):
    print "PRODUCT DATA"
    print "NAME:                 {:s}".format(product.name)
    print "Price:                {:2f}".format(product.price)
    print "Discount Percent:     {:d}".format(product.discountPercent)
    print "DISCOUNT PRICE:       {:.2f}".format(product.getDiscountPrice())
    print "DISCOUNT AMOUNT:      {:.2f}".format(product.getDiscountAmount())
    print


def main():
    print "Product Viewer Program"
    print
    products=(Product('Wood Hammer',12.99,62),
            Product('Hardware wire hails',5.06,0),
            Product('Duct Tape',7.24,0))
    show_product_list(products)

    while True:
        n=int(raw_input("Enter product number"))
        print
        product=products[n-1]
        show_products(product)
        c=raw_input("View another product (y/n)? ")
        print

        if c !='y':
            print "Bye"
            break

if __name__=="__main__":
    main() 
