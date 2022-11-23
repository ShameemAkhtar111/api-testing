import os
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
from faker import Faker

class DataGenerator:
    __fake = None
    __person = {}
    __company = {}
    __cc_details = {}
    def __init__(self,langLocale):
        self.__fake=Faker(locale=langLocale)
        domain=self.__fake.domain_word()
        compName=None
        if "-" in domain:
            domainforComp = domain.replace("-", " ")
            temp_domain = domainforComp.split(" ")
            compName = temp_domain[0].capitalize() + " " + temp_domain[1].capitalize()
            domain = domain.replace("-", "")
        else:
            compName = domain.capitalize()
        domain.strip()
        comp_suffix = self.__fake.company_suffix().strip()
        self.__company['company_name'] = compName + " "+comp_suffix
        if " Sons" in comp_suffix:
            comp_suffix = comp_suffix.replace(" Sons", "sons")
        comp_suffix = comp_suffix[0].lower() + comp_suffix[1:]
        self.__company['company_domain'] = domain+comp_suffix+".com"
        self.__company['email'] = "contact@"+self.__company['company_domain']
        self.__company['url'] = "http://www." + self.__company['company_domain']
        profile=self.__fake.simple_profile()
        self.__person['gender'] = profile.get('sex')
        if self.__person['gender'] == 'M':
            self.__person['firstname'] = self.__fake.first_name_male()
            self.__person['lastname'] = self.__fake.last_name_male()
        else:
            self.__person['firstname'] = self.__fake.first_name_female()
            self.__person['lastname'] = self.__fake.last_name_female()

        self.__person['fullname'] = self.__person['firstname'] + " " + self.__person['lastname']
        self.__person['birthdate'] = profile.get('birthdate').strftime("%m/%d/%Y")
        end_date = date.today()
        difference_in_years = relativedelta(end_date, profile.get('birthdate')).years
        self.__person['age'] = difference_in_years
        self.__person['email'] = self.__person['firstname'] + self.__person['lastname']+"@"+ self.__fake.free_email_domain()
        self.__person['username'] = profile['username']
        self.__person['password'] = self.__fake.password(length=8)
        self.__person['address'] = profile.get('address')
        self.__person['job'] = self.__fake.job()
        self.__person['internation_bank_ac'] = self.__fake.iban()
        self.__person['basic_bank_ac'] = self.__fake.bban()
        self.__person['company'] = self.__company
        self.__person['ssn'] = self.__fake.ssn()
        self.__person['phone_number'] = self.__fake.phone_number()
        # self.__person['credit_card'] = self.__fake.credit_card_full()


    def get_person(self):
        print(self.__person)

    def get_first_name(self):
        return self.__person.get('firstname')

    def get_last_name(self):
        return self.__person.get('lastname')

    def get_full_name(self):
        return self.__person.get('fullname')

    def get_gender(self):
        return self.__person.get('gender')

    def get_birthdate(self):
        return self.__person.get('birthdate')

    def get_age(self):
        return self.__person.get('age')

    def get_email(self):
        return self.__person.get('email')

    def get_username(self):
        return self.__person.get('username')

    def get_password(self):
        return self.__person.get('password')

    def get_full_address(self):
        return self.__person.get('address')

    def get_job(self):
        return self.__person.get('job')

    def get_bank_acc_international(self):
        return self.__person.get('internation_bank_ac')

    def get_bank_acc_basic(self):
        return self.__person.get('basic_bank_ac')

    def get_company_name(self):
        return self.__person.get('company').get('company_name')

    def get_company_domain(self):
        return self.__person.get('company').get('company_domain')

    def get_company_url(self):
        return self.__person.get('company').get('url')

    def get_company_email(self):
        return self.__person.get('company').get('email')

    def get_ssn_number(self):
        return self.__person.get('ssn')

    def get_phone_number(self):
        return self.__person.get('phone_number')

    def get_full_credit_card(self, cardType = None):
        card_details = None
        if cardType is not None:
            if cardType in ['maestro', 'mastercard', 'visa16', 'visa13', 'visa19', 'amex', 'discover', 'diners', 'jcb15', 'jcb16','master','visa']:
                card_details = self.__fake.credit_card_full(cardType)
            else:
                raise Exception("OPPS!!, please enter a valid card type i.e from"
                                "'maestro', 'mastercard', 'visa16', 'visa13', 'visa19', 'amex', 'discover',"
                                " 'diners', 'jcb15', 'jcb16','master','visa'")
        else:
            # self.__person['credit_card'] = self.__fake.credit_card_full()
            card_details = self.__fake.credit_card_full().split("\n")
        cc_num_exp = card_details[2].split(" ")
        cc_cvv = card_details[3].split(": ")
        self.__cc_details['credit_card_type'] = card_details[0]
        self.__cc_details['credit_card_number'] = cc_num_exp[0]
        self.__cc_details['credit_card_exp_date'] = cc_num_exp[1]
        self.__cc_details['credit_card_cvv'] = cc_cvv[1]

        self.__person['credit_card'] = self.__cc_details

        # return self.__person.get('credit_card')

    def get_credit_card_number(self,cardType=None):
        if len(self.__cc_details) == 0:
            if cardType is not None:
                self.get_full_credit_card(cardType)
            else:
                self.get_full_credit_card()
        return self.__person.get('credit_card').get('credit_card_number')

    def get_credit_card_provider(self):
        if len(self.__cc_details) == 0:
            self.get_full_credit_card()
        return self.__person.get('credit_card').get('credit_card_type')

    def get_credit_card_exp_date(self):
        if len(self.__cc_details) == 0:
            self.get_full_credit_card()
        return self.__person.get('credit_card').get('credit_card_exp_date')

    def get_credit_card_cvv_num(self,cardType=None):
        if len(self.__cc_details) == 0:
            if cardType is not None:
                self.get_full_credit_card(cardType)
            else:
                self.get_full_credit_card()
        return self.__person.get('credit_card').get('credit_card_cvv')


if __name__ == "__main__":
    files_list = os.listdir()
    excel_file = None
    for file in files_list:
        if '.xlsx' in file:
            excel_file = file
            break
    print(os.path.abspath(excel_file))
    df = pd.read_excel(os.path.abspath(excel_file), engine="openpyxl")
    df.columns = df.columns.str.lower()
    df.fillna("nan", inplace = True)
    dict_vals = df.to_dict()
    local_val= dict_vals.get('locale')[0]
    no_of_records = int(dict_vals.get('# of data')[0])
    headers = list(dict_vals.get('headers').values())
    frmat = dict_vals.get('format').values()
    constraint = dict_vals.get('constraints').values()
    dm = zip(headers, frmat, constraint)
    print(list(dm))
    print(local_val, no_of_records)
    header_dictionary = {}
    for x in headers:
        header_dictionary[x] = []

    for key in header_dictionary.keys():
        x = []
        for i in range(1, no_of_records+1):
            dg = DataGenerator('en-IN')
            if key.lower() == 'sno':
                x.append(i)
            elif key.lower() == "firstname":
                x.append(dg.get_first_name())
            elif key.lower() == "lastname":
                x.append(dg.get_last_name())
            elif key.lower() == "address" or 'address' in key.lower():
                x.append(dg.get_full_address())
            elif key.lower() == "age":
                x.append(dg.get_age())
            elif key.lower() == "dob" or key.lower() == "dateofbirth":
                x.append(dg.get_birthdate())
            elif key.lower() == "creditcardnumber" or key.lower() == "ccnumber":
                x.append(dg.get_credit_card_number())
            elif key.lower() == "creditcardexpirydate" or key.lower() == "ccexpirydate" or key.lower() == "expirydate":
                x.append(dg.get_credit_card_exp_date())
        header_dictionary[key] = x
    print(header_dictionary)
    df2 = pd.DataFrame(header_dictionary)
    writer = pd.ExcelWriter("test_data2.xlsx", engine='xlsxwriter')
    df2.to_excel(writer, sheet_name="Sheet1", index=False)
    writer.save()





