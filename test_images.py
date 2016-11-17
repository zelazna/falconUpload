import pytest
# import falcon
from app import api
from falcon import testing


@pytest.fixture(scope='module')
def client():
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    return testing.TestClient(api)


def test_post_image(client):
    doc = {'message': 'file uploaded'}

    result = client.simulate_post('/images', headers={"content-type": "image/jpeg"})
    assert result.json == doc


# def test_post_wrong_image_type(client):
#     with pytest.raises(falcon.HTTPBadRequest):
#         client.simulate_post('/images', headers={"content-type": "image/yolo"})


def test_get_message(client):
    result = client.simulate_get('/images/list')
    assert result.json
