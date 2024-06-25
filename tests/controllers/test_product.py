from datetime import datetime
from typing import List

import pytest
from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 8500.0,
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 8500.0,
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    false_id = "31a127fd-8024-408e-8e54-e0ce5455e2e9"
    response = await client.get(f"{products_url}{false_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == f"Product not found with filter: {false_id}"


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}",
        json={"price": 9000, "updated_at": str(datetime.now())},
    )

    content = response.json()

    assert response.status_code == status.HTTP_200_OK

    creation_date = datetime.strptime(content["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
    update_date = datetime.strptime(content["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

    assert update_date > creation_date

    del content["created_at"]
    del content["updated_at"]

    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": 9000,
        "status": True,
    }


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    false_id = "31a127fd-8024-408e-8e54-e0ce5455e2e9"
    response = await client.delete(f"{products_url}{false_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == f"Product not found with filter: {false_id}"
