# FastAPI

FastAPI is a Python library for dealing with ready to use API

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FastAPI.

```bash
pip install "fastapi[all]"
```

Or you can install it, part by part 

```bash
pip install fastapi
```

Also install uvicorn to work as the server:

```bash
pip install "uvicorn[standard]"
```

## Usage

```bash
# run the webserver
uvicorn books:app --reload   
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)