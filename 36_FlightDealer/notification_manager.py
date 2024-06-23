#region IMPORT

from twilio.rest import Client

#endregion

#region INIT

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR AUTHENTICATION TOKEN"
TWILIO_NUMBER = "TWILIO NUMBER"
YOUR_NUMBER = "YOUR NUMBER"

#endregion

class NotificationManager:

    """<DOC

        Manages sending SMS notifications using Twilio.

            METHODS:
                        -__init__ -> None
                        -send_sms -> None

    DOC?>"""

    def __init__(self) -> None:

        """<DOC

            Initialize the NotificationManager with the Twilio client.

        DOC?>"""

        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message: str) -> None:

        """<DOC

            Sends an SMS message using Twilio.

                PARAMETERS:
                            -message (str): The content of the SMS message to be sent.

        DOC?>"""

        #region CODE

        message = self.client.messages.create(
            body=message,      # The content of the SMS
            from_=TWILIO_NUMBER,  # The Twilio number sending the SMS
            to=YOUR_NUMBER,       # The recipient's phone number
        )

        print(message.sid)

        #endregion CODE
