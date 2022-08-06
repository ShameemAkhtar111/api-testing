from datetime import date
from dateutil.relativedelta import relativedelta

from faker import Faker

class DataGenerator:
    __fake = None
    __person = {}
    __company = {}
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

    def get_full_credit_card(self,cardType=None):
        if cardType is not None:
            if cardType in ['maestro', 'mastercard', 'visa16', 'visa13', 'visa19', 'amex', 'discover', 'diners', 'jcb15', 'jcb16','master','visa']:
                self.__person['credit_card'] = self.__fake.credit_card_full(cardType)
            else:
                raise Exception("OPPS!!, please enter a valid card type i.e from"
                                "'maestro', 'mastercard', 'visa16', 'visa13', 'visa19', 'amex', 'discover',"
                                " 'diners', 'jcb15', 'jcb16','master','visa'")
        else:
            self.__person['credit_card'] = self.__fake.credit_card_full()

        return self.__person.get('credit_card')

    def get_credit_card_number(self,cardType=None):
        return self.__fake.credit_card_number(cardType)

    def get_credit_card_provider(self):
        return self.__fake.credit_card_provider()

    # def get_name_on_credit_card(self,cardType=None):
    #     # return self.__fake.credit_card_provider()
    #     return self.__person.get('credit_card').get('name_on_card')

    def get_credit_card_exp_date(self):
        return self.__fake.credit_card_expire()

    def get_credit_card_cvv_num(self,cardType=None):
        return self.__fake.credit_card_security_code(cardType)


# dg = DataGenerator('en-IN')
# dg.get_person()
# print(dg.person)
dg2 = DataGenerator('en-IN')
print(dg2.get_full_credit_card())
print(dg2.get_credit_card_number())
print(dg2.get_credit_card_provider())
# print(dg2.get_name_on_credit_card())
print(dg2.get_credit_card_exp_date())
print(dg2.get_credit_card_cvv_num())
