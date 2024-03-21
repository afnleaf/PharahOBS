import os
from dotenv import load_dotenv
# local modules
import ocr
import client
import test

# load environment
load_dotenv()
ENV: str = os.getenv("ENVIRONMENT")

# main entry point
def main() -> None:
    if ENV == "prod":
        client.main()
    elif ENV == "test":
        #ocr.main()
        test.main()
    else:
        print("Error with ENVIRONMENT in .env file. Must be 'test' or 'prod'.")

if __name__ == "__main__":
    main()
