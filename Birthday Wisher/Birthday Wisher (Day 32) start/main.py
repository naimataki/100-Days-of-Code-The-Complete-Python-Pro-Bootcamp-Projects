import smtplib

my_email = "naimatakiouti24@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password="zdw f oomn wsl l zamz")
connection.sendmail(from_addr=my_email, to_addrs="takioutinaima10@gmail.com", msg="Hello")
connection.close()