from Warehouse.models import Partner

partners = Partner.query.all()

print(partners)

tuples = []

for i in partners:
    s = ('{}'.format(i), '{}'.format(i))
    print(s)
    tuples.append(s)

print(tuples)

if __name__ == '__main__':
    pass
