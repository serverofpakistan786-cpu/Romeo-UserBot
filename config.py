from os import getenv

API_ID = int(getenv("API_ID", "13335263"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "BQJS3PkAdzTOnhT8l_fek1zItp3E6Tn6LeBLIoy3Z0w-mPococgmqBWfvyL5ysfMjhDJp9_UXptk_XG4n3dOk00yy2egWiYptTOw3RhKWY_s89mRRZ1DG1s6nwsoWckZaj2NCv-InNctv1YhrPe-uP5T7LjymwE5tvdlcB9jBhfOEUbIEiHIv39h1nehHmUMRtoGfnGa7yzEzFpK96vuoVfHfrL43WCQI2m7hALbG69kZ8qH-YwaL5P2CBwy6RYXor2fegom-NUJbHAdCJswSDpRMfo8D5W27G85HZOzDdvvu0P3aMH7D7_0VWji1xYybSXweEW-U5eihA-j-XOEcD3M97W1mAAAAAH2yhRpAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8435405929").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/39b11af6d879ffeef0b64-c5b682673bd937e98a.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/RRomeo-RJ/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
