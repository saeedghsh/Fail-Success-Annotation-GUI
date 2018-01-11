Fail Success Annotation GUI
---------------------------
A simple GUI for manually marking results (fail vs. success).
Intended for the manual investigation of the [map alignment](https://github.com/saeedghsh/Map-Alignment-2D/) results.

![screenshot](https://github.com/saeedghsh/Fail-Success-Annotation-GUI/blob/master/docs/screenshot.png)

Dependencies and Download
-------------------------
Most dependencies are listed in `requirements.txt`, and will be installed by the following instructions.
There is also the [Opencv](http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html) that should be installed separately.
```shell
# Download
git clone https://github.com/saeedghsh/Fail-Success-Annotation-GUI.git
cd Fail-Success-Annotation-GUI

# Install dependencies
pip install -r requirements.txt

# launch GUIs
python runMe.py
```

Laundry List
------------
- [ ] opencv is only used for loading images, remove it as dependency.

License
-------
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/Fail-Success-Annotation-GUI/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
