def verify_customer(name, old, customer_level='silver'):
    print("고객님 성함은 %s입니다." %name)
    print("나이는 %d입니다." %old)

    if customer_level == 'silver':
        print("고객님의 등급은 %s입니다.\n" %customer_level)
    elif customer_level == 'gold':
        print("고객님의 등급은 %s입니다. \n" %customer_level)
    elif customer_level == 'platinum':
        print("고객님의 등급은 %s입니다. \n" %customer_level)

verify_customer('둘리', 56, 'gold')