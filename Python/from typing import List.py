from typing import List

def verify_merchants(provided_fields: List[str]) -> None:
    reqs = {
        "individual_US": ['date_of_birth', 'email', 'first_name', 'last_name', 'phone', 'social_security_number'],
        "individual_JP": ['date_of_birth', 'email', 'first_name','first_name_kana', 'last_name', 'last_name_kana', 'tax_id_number'],
        "individual_FR": ['first_name', 'last_name', 'tax_id_number', 'email', 'phone'],
        "company_US": ['name', 'employer_id_number', 'support_email', 'phone'],
        "company_JP": ['name', 'tax_id_number', 'phone'],
        "company_FR": ['name', 'director_name', 'tax_id_number', 'phone']
    }    
    # store input fields, merchant_id is the key, values are fields have been inputted {acct_123: {first_name:..., last_name:..., ...}}
    entity = {} 
    for command in provided_fields[1:]:
        
        id, field, value = command.split(',')
        if id in entity:
            entity[id][field] = value
        else:
            entity[id] = {field: value}
    
    # print(entity)
    
    # process entity
    res = [] # []
    for accnt, fields in entity.items():
        needed_fields = []
        # print(accnt, fields)
        if 'business_type' not in fields and 'country' not in fields:
            line = accnt + ':UNVERIFIED:business_type,country'
            res.append(line)
        elif 'business_type' not in fields:
            line = accnt + ':UNVERIFIED:business_type'
            res.append(line)
        elif 'country' not in fields:
            line = accnt + ':UNVERIFIED:country'
            res.append(line)
        else: # both business_type and country are found
            need = entity[accnt]['business_type'] + '_' + entity[accnt]['country']
            for f in reqs[need]:
                if f not in fields:
                    needed_fields.append(f)
           
            if needed_fields:
                needed_fields.sort()
                print(needed_fields)
                line = accnt + ':UNVERIFIED:' + ','.join(needed_fields)
                # res.append(line)
            else:
                line = accnt + ':VERIFIED'
                res.append(line)
    res.sort()
    for i in res:
        print(i)

if __name__ == '__main__':
    
    s = "12 acct_123,tax_id_number,123456688 acct_123,business_type,company acct_456,business_type,individual acct_456,country,JP acct_456,first_name,Mei acct_456,last_name,Sato acct_456,first_name_kana,Mei acct_456,last_name_kana,Sato acct_456,date_of_birth,01011970 acct_456,tax_id_number,123456677 acct_456,email,text@example.com"
    provided_field = s.split(' ')
    # print(provided_field)
    verify_merchants(provided_field)