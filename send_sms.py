# Import Client from twilio.rest
from twilio.rest import Client

# Your Account Cradantial
account_sid = "AC557bdec33975e23572007eab51c75dd8"
auth_token = "824725b027a7e6923585ab57ebf7b070"


# Get Mobile Number
mobile_number = "+918767286769"

# Frome Mobile Number
my_twilio = "+18284577870"

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

# Send Text Message to User
my_msg = "Hi I am Pruthviraj Rajput. I have Created Text msg sending app using Python. and also used Twilio API."

# Send Message to mobile number here...
message = client.messages.create(
                              body=my_msg,
                              from_=my_twilio,
                              to=mobile_number
                          )

# Meassage Display Here Text Message Send Sussesfuly

if message:
    # Print Meassade Send Id
    print( 'Message Sussesfully Send With Message Id is: ' + message.sid )
    
    # Print Sended Message Body
    print( 'Message Sussesfully Sended Message is: ' + message.body )
    
    # Print Whih Number Meassage Is Send
    print( 'Message Sussesfully Send This Number: ' + message.to )
else :
    print('Message Not Send Due To Server Error..., Please Try again latter')