from openai import OpenAI
import psutil
import subprocess

client = OpenAI()

def call_model(text):
    response = client.responses.create(
        model="gpt-5.6",
        input=text,
        max_output_tokens=1000,
    )
    return response.output_text

# iterate through steps until it fails, and return number of characters limit
def find_limit(step=100_000):
    n = step

    while True:
        text = "x " * n

        try:
            call_model(text)
            print(f"Accepted: {n:,} tokens")
            n += step
        except Exception as e:
            print(f"Failed around {n:,} tokens")
            print(e)
            return n

def break_model_by_token_size ():
  limit = find_limit()
  text = "x " * n
  response = client.responses.create(
        input=text
    )

# get memory by Nvidia or locally
def get_memory_gb():
    memories = {
        "ram": psutil.virtual_memory().total / 1024**3,
    }

    try:
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=memory.total",
                "--format=csv,noheader,nounits",
            ],
            stderr=subprocess.DEVNULL,
            text=True,
        )

        vram = [float(x.strip()) / 1024 for x in output.splitlines()]
        memories["nvidia_vram"] = max(vram)

    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    return memories
  
def break_model_by_local_memory():
  mem = get_memory_gb()

  
 break_model_by_token_size ()
break_model_by_local_memory()
