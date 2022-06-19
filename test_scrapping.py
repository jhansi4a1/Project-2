from scrapping import flipkart
from scrapping import amazon


def test_Amazon_mobile():
    url="https://www.amazon.in/s?k=mobile+is+4G+6+gb+ram+128+gb+memory+card&crid=L0KQ281O32K0&sprefix=mobile+is+4g%2Caps%2C232&ref=nb_sb_noss"
    assert amazon().Amazon_mobile(url)=="Mobile is a 4G, 6 GB RAM and 128 GB memory."
    
def test_Amazon_laptop():
    url="https://www.amazon.in/s?k=laptop+is+i5%2C+8gb+ram+with+1+tb+hdd&crid=2Q28C0S06MVXN&sprefix=%2Caps%2C1887&ref=nb_sb_ss_recent_6_0_recent"
    assert amazon().Amazon_laptop(url)=="Laptop is i5, 8GB RAM with 1 TB HDD"
    

def test_Flipkart_mobile():
    url="https://www.flipkart.com/search?q=Mobile+is+a+4G%2C+6+GB+RAM+and+128+GB+memory.&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
    assert flipkart().Flipkart_Mobile(url)=="Mobile is a 4G, 6 GB RAM and 128 GB memory."
    
def test_Flipkart_laptop():
    url="https://www.flipkart.com/search?q=Laptop%20is%20i5%2C%208GB%20RAM%20with%201%20TB%20HDD&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    assert flipkart().Flipkart_Laptop(url)=="Laptop is i5, 8GB RAM with 1 TB HDD"
    
