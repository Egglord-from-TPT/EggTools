def Update():
    import os
    import sys
    try:
        from tqdm import tqdm
        import requests
        from bs4 import BeautifulSoup
    except Exception:
        os.system(f"{sys.executable} -m pip install --upgrade tqdm requests bs4")
        from tqdm import tqdm
        import requests
        from bs4 import BeautifulSoup
    import subprocess
    import time
    url="https://pypi.org/user/Egglord/"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    projects=set()
    for a in soup.find_all("a",href=True):
        if a["href"].startswith("/project/"):
            name=a["href"].split("/")[2]
            projects.add(name)
    packages=[]
    print("EGGLORDS PACKAGES:")
    for p in projects:
        if p!="EggTools":
            packages.append(p)
            print("    ",p)
    print("\n")
    cmd=[sys.executable,"-m","pip","install","--upgrade"]+packages
    spinner=["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠏"]
    with subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True) as process:
        i=0
        while process.poll() is None:
            print(f"Installing packages... {spinner[i % len(spinner)]}",end="\r",flush=True)
            time.sleep(0.1)
            i+=1
        stdout,stderr=process.communicate()
        if process.returncode==0:
            print("Done!"," "*25)
        else:
            print("Failed!"," "*25)
            print(stderr)
def Scan(code_str):
    import os
    import sys
    try:
        import ast
    except Exception:
        os.system(f"{sys.executable} -m pip install --upgrade ast")
        import ast
    risky_nodes=(ast.Call,ast.Import,ast.ImportFrom,ast.Global)
    try:
        tree=ast.parse(code_str)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node,risky_nodes):
            return False
        if isinstance(node,ast.Call):
            if hasattr(node.func,'id') and node.func.id in ("eval","exec","compile","__import__"):
                return False
    return True
def EggCrash():
    import sys
    sys.setrecursionlimit(10**9)
    import threading
    print("🥚",end="",flush=True)
    threads=[]
    NUM_THREADS=1000
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=EggCrash)
        t.start()
        EggCrash()
        threads.append(t)
    EggCrash()
    for t in threads:
        EggCrash()
        t.join()