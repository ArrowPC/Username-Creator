
![alt text](https://raw.githubusercontent.com/ArrowPC/Username-Creator/master/src/app.ico) 
**Username Creator**


 Simple Qt tool that takes in a text file and formats it to basic usernames 


## Installation

 1. Go to [Releases](https://github.com/ArrowPC/Username-Creator/releases/latest) and download the zipped file based on your platform.
 2.  unzip and launch the executable.



## Run Locally

Clone the project

```sh
  git clone https://github.com/ArrowPC/Username-Creator
```

Go to the project directory

```sh
  cd username-creator/src
```

Install dependencies

```sh
  pip install requirements.txt
```

Start the application

```sh
  python main.py
```


## Building
Packaging the project and creating an executable

### Using [Pyinstaller](https://github.com/pyinstaller/pyinstaller)
1. Install Pyinstaller
```sh
  pip install pyinstaller
```
2. Make sure you're in the correct directory
```sh
  cd username-creator/src
```
3. Run pyinstaller 
```sh
  pyinstaller --name="Username Creator" --clean -y --windowed --dist ./dist/bin --workpath /tmp --onefile --icon=app.ico main.py
```
***NOTE: Pyinstaller has tons of configurable options that can be found [here](https://pyinstaller.org/en/stable/usage.html), the command above is just a simple demo***

