import subprocess

def speak(text: str, output_pat: str = "output.wav"):
    subprocess.run(
        ["piper", "--model", "en_us-lessac-medium.onnx",
         "--output_file", output_pat],
         input=text.encode("utf-8"),
         check = True
    )

    return output_pat