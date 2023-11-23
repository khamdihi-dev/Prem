### Cara Install Di Termux
    pkg update && upgrade
    pkg install tur-repo -y
    pkg install git
    pkg install clang libffi openssl libsodium binutils
    pkg install python3.9
    pip install requests bs4 rich
    rm -rf Prem
    git clone https://github.com/khamdihi-dev/Prem
    cd Prem
    python3.9 run.py
    
