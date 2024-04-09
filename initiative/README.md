# INITIATIVE
##### a python program

## requirements
- a computer with a command window
  - I think literally any computer works, except like a McDonalds computer where you place your order
  - if you have a mac, type cmd + space, and then type `terminal`
  - if you have a windows computer, open this folder, and in the navigation bar, type `cmd.exe` and hit enter
- python installed
  - google it
  - you do need to know the python version sometimes, so you know which word to type to use python. It's usually either `python`, `python2`, or `python3`

## how to use
- i assume if you are at this step, you've unzipped this file
  - if you haven't done that, do that
- open that command window from the requirements
- navigate to the folder that you have this file in, using the command window.
  - on windows, if you do it the way i specified, then you're already here.
  - on mac, you will have to find the location where the file is stored (usually `~/Downloads`), and then enter the following command in the command window: `cd [file_location]`, but replace the brackets and the stuff in the brackets with the file location you found earlier in this step.
- run the initiative command
  - there are two ways to run it, but each of them is a command you have to enter into the command window.
    - first, you can just run the program, and manually enter everything. Type `python initiative.py` to do so. If you downloaded a version of python that requires you to use `py`, `python2`, or `python3`, replace `python` with that for all of these commands.
    - second, you can use some parameters. To use a parameter, you append `-X`, where `X` is the parameter letter, and then append a space, and then append something related to the parameter, to the first way. These will pre-fillout some of the stuff you would normally do manually. Look, it's easier to show it in a table:

|thing to customize|command letter|command syntax|example|
|---|---|---|--|
|character names|`c`|in quotes, a comma-separated list of character names|`python initiative.py -c "Sir Lancelot, King Arthur, Another Guy"`|
|initiative bonuses|`i`|in quotes, a comma-separated list of initiative bonuses|`python initiative.py -i "2, -3, 0"`|
|number of rolls|`r`|just the number of rolls|`python initiative.py -r 1000`|
|file to load from|`f`|just the name of a file, or the "path" to the file if it isn't in the same folder|`python initiative.py -f ~/Documents/Personal/Boring/OkItsDnD/super_cool_party_setup.txt`|

  - Something to note! You can totally mix and match these options. In fact, the character names and initiative bonuses are _designed_ to work well with each other, so the first and second character names will be mapped to the first and second initiative rolls, respectively. However, if there are character names without initiatives, then the default initiative value is 0, and if there are initiatives without characters, the default character name is 'Unnamed Character X', where X is the number of unnamed characters so far.
  - here is another example:
```
> python initiative.py -c "Sir Lancelot, Sir Dingus, Big Chungus" -i "2, 5, -1", -r 1000
```
_The above example is set up to do 1000 runs with the three above character names and initiative rolls_

  - Something else to note! Loading from a file requires the file to look a certain way. There is a file included in this folder called `inputfile.txt` which looks like the file should look. Basically, on the first line there's the number of runs, and then on each other line there's the character name, then a comma, then their initiative bonus. I think it works without a number of rolls as long as you leave the first line blank _(citation needed)_, and I think it also works if you only have a number of rolls in the first line, and no characters. I don't think it works if you just have a list of names with no initiatives, or initiatives with no names (especially since a character could _technically_ be called "-1" or similar.)