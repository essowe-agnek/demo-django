from customer.models import *
client = Client(schema_name='public',name="schema public")
client.save()
domain = Domain()
domain.domain = 'localhost'
domain.tenant = client
domain.is_primary = True
domain.save()

from customer.models import *
client = Client(schema_name='shop1',name="Boutique Cosmétique")
client.save()
domain = Domain()
domain.domain = 'shop1.localhost'
domain.tenant = client
domain.is_primary = True
domain.save()