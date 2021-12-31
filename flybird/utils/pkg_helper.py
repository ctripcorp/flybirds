"""
py ns load
"""
import importlib
import pkgutil


def load_pkg_by_ns(pkg_ns):
    """
    py ns load
    """
    base = importlib.import_module(pkg_ns)
    for loader, module_name, is_pkg in \
            pkgutil.walk_packages(base.__path__, f'{base.__name__}.'):
        try:
            __import__(module_name)
        except ImportError as e:
            raise e
