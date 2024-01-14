import subprocess
import time

def ping_domain(domain):
    try:
        # Run the ping command with a timeout of 6 seconds
        subprocess.run(["ping", "-c", "1", "-W", "6", domain], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    domain_to_ping = "O-K-I-L-A.com"  # Replace with the domain you want to ping
    ping_timeout = 6  # Timeout in seconds

    if not ping_domain(domain_to_ping):
        print(f"No response from {domain_to_ping}. Running ch.py...")
        
        # Replace 'python3' with 'python' if you're using Python 2
        subprocess.run(["python3", "change-sub.py"])
    else:
        print(f"Response received from {domain_to_ping}. No need to run change-sub.py.")

if __name__ == "__main__":
    main()
