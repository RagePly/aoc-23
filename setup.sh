MY_PY_SETUP="$HOME/tools/setup-python3.sh"
PY_VENV="$PWD/bin/activate"
PY_REQ="$PWD/requirements.txt"

if [ -e $MY_PY_SETUP ]; then
    echo "[INFO]: Setting up python3"
    . $MY_PY_SETUP
else
    echo "[INFO]: Using normal python installation"
fi

if [ -e $PY_VENV ]; then
    echo "[INFO]: Activating venv"
    . $PY_VENV
else
    echo "[INFO]: venv does not exist, creating"
    python3 -m venv .

    echo "[INFO]: Activating venv"
    . $PY_VENV

    if [ -e $PY_REQ ]; then
        echo "[INFO]: installing packages"
        pip3 install -r $PY_REQ
    fi
fi
