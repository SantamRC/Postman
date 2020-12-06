from smtplib import SMTP_SSL
import os

def send(args):
    #login info
    from_addr   = args['from_addr']
    password    = args['password']
    
    #senders
    to_addr     = args['to_addr']
    cc_addr     = args['cc_addr']
    bcc_addr    = args['bcc_addr']
    
    #email compiled
    message     = "From: %s\r\n" % from_addr
    message    += "To: %s\r\n" % ', '.join(to_addr)
    message    += "CC: %s\r\n" % ', '.join(cc_addr)
    message    += "Subject: %s\r\n" % args['subject']
    message    += "\r\n" 
    message    += args['body']

    recivers    = to_addr + cc_addr + bcc_addr
    print(message)
    with SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_addr, password)                       #login process

        while len(recivers)>99:                                 #only 100 emails can be sent once
            rec = recivers[:100]
            recivers = recivers[100:]
            server.sendmail(from_addr, rec, message)
        
        server.sendmail(from_addr, recivers, message)
    return None
        


args = {
    'from_addr' : 'sender',
    'password' : 'password;,
    'to_addr' : [],
    'cc_addr' : [],
    'bcc_addr' : [],
    'subject' : 'Demo subject',
    'body' : 'Unreal body',    
}
send(args)

