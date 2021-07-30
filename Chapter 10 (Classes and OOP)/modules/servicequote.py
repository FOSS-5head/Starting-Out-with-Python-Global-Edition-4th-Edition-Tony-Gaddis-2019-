# Константа для ставки налога с продаж.
TAX_RATE = 0.05


# Внимание на опечатки, отмечены "(!)".
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    # (!) В книге будет опечатка, не стоит self.
    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    # (!) И опять опечатка, не поставили self.
    # А яй-яй переводчики.
    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
               (self.__parts_charges * TAX_RATE)
