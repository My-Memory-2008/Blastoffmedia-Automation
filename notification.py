import os
import subprocess
import sys
import time
import datetime
import asyncio

from kaggle_secrets import UserSecretsClient

# 1. DEPENDENCY AUTOPREPARATION
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests


print("⏰ [Custom Trigger] Executing custom task at scheduled India Time...")

# WRITE YOUR CUSTOM CODE OR FUNCTION STATEMENT INSIDE HERE
# 1. Enter the EXACT unique topic name you created in the app
NTFY_TOPIC = "my_kaggle_575_alert"



# 3. Create the alert message with a direct link to your notebook
# Replace 'username/notebook-slug' with your actual Kaggle notebook URL path
notebook_url = "https://github.com/My-Memory-2008/Blastoffmedia-Automation/tree/main/blastoffmedia_outputs"


# --- Execution ---
url = f"https://ntfy.sh/{NTFY_TOPIC}"

# Clean headers containing only standard text characters
headers = {
    "Title": "Kaggle Run Finished Successfully!",
    "Priority": "high",
    "Click": notebook_url 
}

# Emojis are perfectly fine to use inside the message body text
message = "🎬 Your video and SEO JSON file are processed and ready for download. ✅ DRAFT   IT   TO  UPLOAD  AT  12:30 PM  OR  6:00PM "

try:
    response = requests.post(url, data=message.encode('utf-8'), headers=headers, timeout=20)
    if response.status_code == 200:
        print("🎯 Success! Check your phone for the free ntfy notification.")
    else:
        print(f"❌ Failed to send alert: {response.text}")
except Exception as e:
    print(f"❌ Connection error: {e}")


print("✅ **Kaggle Execution Complete!**\n\n""Your video and SEO JSON data are ready for download and copying seo data.\n\n"f"🔗 [Click here to open Kaggle Output]({notebook_url})")

    
    
    
print("✅  Upload to Message to mobile phone successfull.././././")
