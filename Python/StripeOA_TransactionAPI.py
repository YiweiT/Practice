import re
import json
from typing import Iterable, Callable, List

# use for the first part of input
# "card_country=US&currency=USD&amount=2500&ip_country=CA"
class Charge:
    def __init__(
        self,
        card_country: str = None,
        currency: str = None,
        amount: float = None,
        ip_country: str = None
    ) -> None:
        self.card_country = card_country
        self.currency = currency
        self.amount = amount
        self.ip_country = ip_country

# amount>500, ip_country==CA
class Filter:
    def __init__(self, field: str, operator: str, value: str) -> None:
        self.field = field
        self.operator = operator
        self.value = value

    def evaulate(self, charge: Charge) -> bool:
        value = getattr(charge, self.field) # values followed by CHARGE
        expected = type(value)(self.value) # condition followed by ALLOW / BLOCK
        if self.operator == '==':
            return value == expected
        elif self.operator == '>':
            return value > expected
        elif self.operator == '<':
            return value < expected
        elif self.operator == '>=':
            return value >= expected
        elif self.operator == '<=':
            return value <= expected
        elif self.operator == '!=':
            return value != expected
        return False

# amount>500ANDip_country==CA, card_country==CAORcard_country==MA
class FilterCollection:
    def __init__(self, is_and: bool, filters: Iterable[Filter]) -> None:
        self.is_and = is_and
        self.filters = filters
    
    def evaluate(self, charge:Charge):
        res = True if self.is_and else False

        for filter_ in self.filters:
            if self.is_and: # the logic operator is AND
                res = res and filter_.evaluate(charge)
                if not res:
                    return False
            else: # logic operator is OR
                res = res or filter_.evaluate(charge)
                if res:
                    return True
        return res

# ALLOW:amount>500ANDip_country==CA, BLOCK:card_country==CAORcard_country==MA 
class Rule:
    def __init__(self, allow: bool, filters: FilterCollection) -> None:
        self.allow = allow
        self.filters = filters
    
    def is_allowed(self, charge: Charge):
        val = self.filters.evaluate(charge)
        if self.is_allowed and val:
            return True
        if not self.is_allowed and not val:
            return True
        return False

# Parce List[str] to Rules
class ChargeParser:
    ENDING_COMMA_PATTERN = re.compile(',[ ]*[]]')
    NUMERIC_PATTERN = re.compile('[0-9]+([.][0-9]+|)')
    OPERATOR_PATTERN = re.compile('(!=|[><=](=|))')
    LOGICAL_OPERATOR_PATTERN = re.compile('(AND|OR)')

    def parse(self, charge: str):
        res = json.loads(self.ENDING_COMMA_PATTERN.sub(']', charge))
        # res = ['CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA', 'ALLOW:amount>500ANDip_country==CA', 'BLOCK:card_country==CAORcard_country==MA']
        return self.parse_charge(res[0]), self.parse_rules(res[1:])

    def parse_charge(self, charge: str):
        entity = Charge()

        # CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA
        #        ^ start here
        for exp in charge[7:].split('&'): 
            field, value = exp.split('=')
            # amount=25000, field = amount, value = float(25000)
            if self.NUMERIC_PATTERN.search(value):
                value = float(value)
            
            setattr(entity, field, value) # set Charge attributes
        return entity

    def parse_rules(self, rules: List[str]) -> Iterable[Rule]:
        return [self.parse_rule(rule) for rule in rules]
    
    def parse_rule(self, rule: str) -> Rule:
        # ALLOW:amount>500ANDip_country==CA
        allow, exp = rule.split(':')
        allow = (allow == 'ALLOW')
        logical_operator = self.OPERATOR_PATTERN.search(exp)
        if logical_operator:
            logical_operator = logical_operator[0]
            exps = exp.split(logical_operator)
        else:
            exps = [exp]
        
        is_and = (logical_operator == 'AND')
        filters = FilterCollection(is_and, [self.parse_filter(ep) for ep in exps])

        return Rule(allow, filters)

    def parse_filter(self, filter_: str) -> Filter:
        print(filter_)
        operator = self.OPERATOR_PATTERN.findall(filter_)[0][0]
        field, value = filter_.splite(operator)
        return Filter(field, operator, value)

class Radar:
    def __init__(self, parse_cls: Callable = ChargeParser) -> None:
        self.parse = parse_cls()

    def is_allowed(self, charge: str):
        charge, rules = self.parse.parse(charge)
        for rule in rules:
            if not rule.is_allowed(charge):
                return False
        return True

                  

if __name__ == '__main__':
    charge0 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:amount>500ANDip_country==CA\",\"BLOCK:card_country==CAORcard_country==MA\",  ]\n"
    charge1 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:amount>500ANDip_country==CA\",\"BLOCK:card_country==USANDamount<200\",  ]\n"
    charge2 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:currency==EUR\",  ]\n"
    charge3 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"BLOCK:amount>500\",  ]\n"
    charge4 = "[\"CHARGE:card_country=US&currency=USD&amount=2500&ip_country=CA\",\"ALLOW:amount>500ANDamount<2501\",  ]\n"
    charge5 = "[\"CHARGE:card_country=US&currency=USD&amount=505&ip_country=CA\",\"ALLOW:amount>500ANDip_country==CA\",\"BLOCK:card_country==CAANDamount<200\",  ]\n"
    charge6 = "[\"CHARGE:card_country=US&currency=USD&amount=505&ip_country=CA\",\"ALLOW:amount>500ANDamount==999ANDip_country==CA\",\"BLOCK:card_country==MAANDamount<200\",  ]\n"
    charge7 = "[\"CHARGE:card_country=US&currency=USD&amount=999&ip_country=CA\",\"ALLOW:amount>500ANDamount==999ANDip_country==CA\",\"BLOCK:card_country==MAANDamount<200\",  ]\n"
    charges = [charge0, charge1, charge2, charge3, charge4, charge5, charge6, charge7]

    for charge in charges:
        r = Radar(ChargeParser().parse(charge))
        print(r)