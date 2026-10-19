class Phone:
    price=1000 
    color="Black"
    brand="Samsung"
    fetures=['camera', 'speaker', 'network']
    
    def call(self): #ekta parameter diye rakhte hoy prothom perameter k instant ba self hisebe dhore nei pyton
        print('calling one persion')
    def send_sms(self,phone,sms):
        txt=f'sending SMS to :{phone} and message: {sms},'
        return txt

my_phone= Phone()
print(my_phone.fetures)
print(my_phone.call())
result= my_phone.send_sms(343432,"I miss you")
print(result)
