# NeverNote
Task manager server with possibility of exporting/importing your current task.
### How to install:
```
pip3 install flask
python3 app.py
```
Then open the address from the console(most likely http://127.0.0.1:5000) in your browser.
### How to use:
There are several features:
  1. Add the task. There will be an **add task** button in the upper panel. An additional window will open as soon as you press it and you will be asked to fill in the information. The complexity will be reflected in the background colour of the task title.
  2. Move the task after it has passed the stage. There will be **Start!**, **Done!** and **Finish** buttons for every task.
  3. Download the state of the task board. The **get task sheet** button is responsible for this
  4. Upload the status of the task board. You need to select the downloaded state using the **browse** button. Then press **add task sheet** to upload.
  5. There is also a special counter for completed tasks. 
### TODO:
  1. Tasks from the **finished** list can be viewed in a special window.
