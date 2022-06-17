# cue-blender
A blender plugin to sequence live streams in OBS with the blender timeline.
Demo video: https://www.youtube.com/watch?v=pSbksA4dxRc

# How to start
Ready to make your own Blender add-on? Make a new repository from this template, download, then get developing!

**Note:** This guide covers the general procedure for setting up this template as tested on Ubuntu Linux. The exact commands may vary depending on your OS and development environment, so some knowledge in python and pip is recommended before trying this. If you run into problems that you can't fix yourself, feel free to open an issue at the [original repo](https://github.com/TheTrueCoder/blender-addon-template) for some help and to potentially improve the code.

## 1. Copy template
![Github repository with Use template button highlighted](https://docs.github.com/assets/cb-36544/images/help/repository/use-this-template-button.png)

For more detail on this process [view the official docs page](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## 2. Local setup
Clone your new repository to your computer using any method you prefer. If you don't know how to, [GitHub has documentation on doing this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). 

Now open a terminal in the cloned project folder and run `pip install -r build-requirements.txt` to install the build tools for your addon.

## 3. Build the addon
To build the addon, run the setup script `python build.py`. That will download any new packages and create a zip file of your addon.

Then just import and enable the addon in Blender and the sample code should print "hello" to the blender console. If it does, it successfully called the required module.

## 4. Customise!
To change the packages included in your addon, open `vendorize.toml` and change the items under packages to your required ones.
To then import this new module, use the following line replacing module name with the name of your module. `from ._vendor import <module name>`

To remove the sample code and module, delete the `hello-world-20200509` package from `vendorize.toml` and remove the two lines of code from `__init__.py` that are after comments with `SAMPLE:` at the start.
