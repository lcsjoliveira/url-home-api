from url_home.utils import generate_short_id


def test_generate_short_id_length():

    short_id = generate_short_id()

    assert len(short_id) == 6


def test_generate_short_id_type():

    short_id = generate_short_id()

    assert isinstance(short_id, str)
