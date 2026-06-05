import importlib.util
import os
import tempfile

import pytest


def load_module(db_path):
    os.environ["DB_PATH"] = db_path
    spec = importlib.util.spec_from_file_location(
        "starter_code",
        os.path.join(os.path.dirname(__file__), "..", "starter-code.py"),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_create_and_read_records():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")
        module = load_module(db_path)
        module.init_db()

        item = module.create_item("Test Item", "A sample item", 12.5)
        assert item["id"] == 1
        assert item["name"] == "Test Item"

        items = module.list_items()
        assert len(items) == 1
        assert items[0]["name"] == "Test Item"


def test_update_and_delete_records():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")
        module = load_module(db_path)
        module.init_db()

        item = module.create_item("Old", "Old item", 5.0)
        updated = module.update_item(item["id"], name="New", price=7.5)
        assert updated is not None
        assert updated["name"] == "New"
        assert updated["price"] == 7.5

        deleted = module.delete_item(item["id"])
        assert deleted is True
        assert module.get_item(item["id"]) is None


def test_search_items():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")
        module = load_module(db_path)
        module.init_db()

        module.create_item("Apple", "Fruit", 1.0)
        module.create_item("Banana", "Fruit", 1.5)
        results = module.search_items("App")
        assert len(results) == 1
        assert results[0]["name"] == "Apple"
