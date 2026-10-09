"""Public query error text must never be stored as a rendered image."""
import ast
import unittest
from pathlib import Path


class PublicRenderCacheTest(unittest.TestCase):
    def test_renderers_skip_error_text(self) -> None:
        root = Path(__file__).resolve().parents[1] / "GenshinUID"
        targets = [("genshinuid_compute/get_my_pack.py", "draw_my_pack"), ("genshinuid_guide/get_bbs_post_guide.py", "get_material_way_post")]
        for relative, name in targets:
            tree = ast.parse((root / relative).read_text(encoding="utf-8"))
            method = next(n for n in ast.walk(tree) if isinstance(n, ast.AsyncFunctionDef) and n.name == name)
            self.assertTrue(any(isinstance(d, ast.Call) and any(k.arg == "skip_text" and isinstance(k.value, ast.Constant) and k.value.value is True for k in d.keywords) for d in method.decorator_list), name)
