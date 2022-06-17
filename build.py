import vendorize.cli as vendorize
from shutil import make_archive, copytree, rmtree
from os.path import join, exists

# Name of addon. Determines the name of the zip package.
ADDON_NAME: str = "addon-test"
# Name of folder that the plugin source code lives in.
CODE_DIR: str = "src"
# Name of folder to put python packages.
DEP_FOLDER_NAME: str = "_vendor"

# Path where vendorised package is generated.
DEP_PATH = join(CODE_DIR, DEP_FOLDER_NAME)

# MAKE VENDORISED PACKAGE BUNDLE
# Delete old package bundle to avoid stale packages in the build.
if(exists(DEP_PATH)):
    rmtree(DEP_PATH)
# Download packages into the _vendor folder to be used in the addon.
# Configure the downloaded packages in vendorize.toml.
vendorize.main()

# MAKE ZIP PACKAGE
# Make temporary folder copy with the project name so that
# the addon is identifiable when installed.
copytree(CODE_DIR, ADDON_NAME)
# Zip addon for easy distribution
make_archive(ADDON_NAME, "zip", ".", ADDON_NAME)
rmtree(ADDON_NAME)
