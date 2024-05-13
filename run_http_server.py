import uvicorn


def run_server():
    uvicorn.run("src:app", host='0.0.0.0', port=5000)


if __name__ == '__main__':
    run_server()
