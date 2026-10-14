EMAIL_SCENARIOS = [
    {
        "id": 1,
        "company": "Microsoft",
        "sender": "security@m1crosoft-support.com",
        "subject": "Your Microsoft 365 password expires today!",
        "body": """
Your Microsoft 365 password will expire today.

To keep your account active, please verify your
identity using the link below:

https://example.local/verify

Failure to verify your account may result in
temporary account suspension.
""",
        "is_phishing": True,
        "indicators": [
            "Suspicious sender domain",
            "Urgent language",
            "Request to verify identity",
            "Threat of account suspension"
        ]
    },

    {
        "id": 2,
        "company": "DHL",
        "sender": "notifications@dhl.com",
        "subject": "Your package has been delivered",
        "body": """
Hello,

Your DHL package has been delivered successfully.

You can check your shipment information using
your existing DHL account.

Thank you,
DHL
""",
        "is_phishing": False,
        "indicators": []
    },

    {
        "id": 3,
        "company": "Bank",
        "sender": "security@bank-account-alert.com",
        "subject": "URGENT: Suspicious activity detected",
        "body": """
We detected unusual activity on your account.

Your account may be restricted within 24 hours.

Please confirm your account information immediately:

https://example.local/account

Thank you.
Security Department
""",
        "is_phishing": True,
        "indicators": [
            "Urgent language",
            "Suspicious sender domain",
            "Threat of account restriction",
            "Request for account information"
        ]
    }
]
