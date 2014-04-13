# MeoSMS

A script that crawls the meo.pt webpage in order to send sms's via the html form provided. I invoke this script with Alfred on mac osx.

## Install & Setup

Install dependencies:

    pip install -r requirements.txt
    
Fill in the ``my_username`` and ``my_password`` variables in ``app.py`` with your meo.pt credentials

Run the script:
    
    python app.py <phone_no> <text>

Create a bash alias script in ``/usr/local/bin/``:

```
#!/bin/bash
python ~/Path-to-script/app.py $*
```