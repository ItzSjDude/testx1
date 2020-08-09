from userbot import LOGS

def __list_all_plugins():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_plugins = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_plugins


ALL_PLUGINS = sorted(__list_all_plugins())
LOGS.info("Loading plugins please wait.......")
__all__ = ALL_PLUGINS + ["ALL_PLUGINS"]
