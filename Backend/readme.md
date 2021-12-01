# Reatil POS
## Backend documention
This document is intended for documenting apis and backend architecture. 
- ✨Magic ✨

## Installation

Requirement: python

Install the dependencies and devDependencies and start the server.

```sh
cd backend
```

# REST API 

The REST API to the app is described below.

##### Requests

`GET /Product`

    http://127.0.0.1:5001/product?barcode=64642079992
##### Response
    {
        [
            554,
            64642079992,
            "TEST PRODUCT",
            11111.0,
            1,
            1,
            1,
            1
        ]
    }

##### Requests

`POST /Product`

    http://127.0.0.1:5001/product

### Response

    {
        555
    }
Just the id. 

##### Request

`POST /order`

    http://127.0.0.1:5001/order
    {
        "user_id": "test",
        "total_sale": 2,
        "total_items": 2,
        "item_list": {
            "9278349723": 1,
            "123123": 9
        }
    }
##### Response

    {
        Success
    }

Just gives the success for now. 

