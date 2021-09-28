# Import Client from twilio.rest
from twilio.rest import Client

# Your Account Cradantial
account_sid = "Add Here your account Id"
auth_token = "Add Here Your Auth Token"


# Get Mobile Number
mobile_number = "+Add your monile number"

# Frome Mobile Number
my_twilio = "+Add here twilio mobile number"

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
