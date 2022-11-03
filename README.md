# django-GoogleCalender-Integration

Working Snapshot:

![image](https://user-images.githubusercontent.com/91273192/199777624-3a50abf7-dd83-4761-9d72-cd37f2ea2265.png)

Got all event details on example Calender

![Screenshot (128)](https://user-images.githubusercontent.com/91273192/199773838-8135919b-a860-4912-934f-f66bb720bbb3.png)

Added demo events through django

![Screenshot (129)](https://user-images.githubusercontent.com/91273192/199774068-0ebe75db-ca61-472c-b723-38b7057ddc22.png)






# Steps

1. Register for Google Service Account

Follow Google's directions to setup the new credentials here: developers.google.com

2. Configure a Test Calendar | View your Google Calendar

In the sidebar will be a list of your calendars; click the "+" button and select "Create New Calendar" from the dropdown

Fill in a name "Example", and click the "Create Calendar" button

Hover over this newly created calendar back in the sidebar, and click the three vertical dots, and select "Settings and Sharing" from the dropdown

Scroll down to "share with specific people"

Add your newly created service account email address (it will be "client_email" in your saved credentials file)

Scroll down to "Integrate Calendar" and copy the Calendar ID string, then paste it somewhere safe as you'll need it again soon.


3. Create Your Local Credentials File | google-credentials.json

Copy paste the entire JSON object from your downloaded credentials file into this newly created .json file.
Example:
  {

  "type": "service_account",

  "project_id": "example",

  "private_key_id": "BLAHBALH",

  "private_key": "-----BEGIN PRIVATE KEY-----\nSUUUUUUPER------LONG-------STRING\n-----END PRIVATE KEY-----\n",

  "client_email": "USERNAME@EXAMPLE.iam.gserviceaccount.com",

  "client_id": "1234567890987654321",

  "auth_uri": "https://accounts.google.com/o/oauth2/auth",

  "token_uri": "https://oauth2.googleapis.com/token",

  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",

  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/username%40example.iam.gserviceaccount.com"

  }


4. Add The API Calls






