from AppBase.usage import usage
from Business.models import VitrineCategory, BusinessProduct


def api(self):
    return {
        "key": self.key,
        "name": self.name,
        "business_key": self.business.key,
        "products": [x.key for x in self.category_products.A().order_by("order")],
        "create": self.create.timestamp(),
        "update": self.update.timestamp()
    }


@usage
def add_to_category_v1abcd12(_, d, device):
    if 'Validate Request and Initialize':
        # try:
        customer = device.user
        category = VitrineCategory.k(d['category_key'])
        _ = category.key

        products_keys = d['products_keys']

        # except (ValueError, KeyError, AttributeError):
        #     return 400

        if "Fetch Products":
            products = BusinessProduct.f(key__in=products_keys)
            if products:
                for product in products:
                    product.category = category

            if "save":
                BusinessProduct.objects.bulk_update(products, ['category'])
                customer.save_synchronize_flag("categories", customer.pk)

        return 200, category.api()
