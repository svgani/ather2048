# 2048 Game

2048 is played on a gray 4×4 grid, with numbered tiles that slide when a player moves them using the keys 1, 2, 3 and 4 as Left, Right, Up and Down respectively.

## How to Run the Project
* Prerequisite
    * Software: Python 3 and above, Node.
    * Operating System: Windows or Linux based. 
### Execution on console.
* Please execute the following command: 
    ```
    python3 2048.py
    ```
### Execution on nodejs.
* Please go to ui_2048 folder
* Please install node modules:
    ```
    npm install
    ```
* Please execute the following command
    ```
    npm start
    ```


## Flow chart

![Alt text](design/design-2048.png?raw=true "Flowchart")

## Sample Output Using Python
```
Note: The following output will be displayed when the game is started.

sh-3.2$ python3 2048.py

Score: 0
-----------------------------
|      |      |      |      |
-----------------------------
|      |      |      |      |
-----------------------------
|      |      |      |    4 |
-----------------------------
|      |      |    2 |      |
-----------------------------

Enter 
1 --> left
2 --> right
3 --> up
4 --> down

Note: The following output will be displayed when the game is completed.

-----------------------------
|    4 |    2 |    8 |    4 |
-----------------------------
|    2 |    4 |   16 |    8 |
-----------------------------
|    8 |   16 |    2 |    4 |
-----------------------------
|    2 |    8 |    4 |    2 |
-----------------------------
Thanks for playing
Score: 128
```