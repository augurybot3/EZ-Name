# EZ-Name

<br>

"EZ-Name helps users automate and customize the renaming of files across searches and directories, offering features like custom separators, metadata-based renaming, recursive renaming, and more.

## Why?

As a developer, I found myself frequently needing to rename multiple files to use a specific convention, such as Kebab-Case. For consistency and organizational purposes I wanted to rename thousands of files without changing writing over the names but simply removing any spaces ' ' and underscores '_' and replacing them with a ddash '-'. So I wrote a script. 

<br>

So, at this point that is all this program does is...


### rename all relevant files within a single folder (with an option to include it's sub-folders) to **`'kebab-case'`**

For more information about the exact details about it's functionality, see [Details](##Details).

<br>

So, this got me thinking.... 

---


## What Additional Features Would Be Useful?

Here is a list of a few ideas that immediately came to mind...

<br>

**Custom separators:** Allow the user to specify the kind of separator they want to use. This could be done with a command-line argument or a prompt.

<br>

**Capitalization options:** Add an option to capitalize every word in the filename, or to convert the filename to lowercase or uppercase.

<br>

**Metadata-based renaming:** Use the os.stat function or a library like pyexifinfo to get metadata about the file, and include this information in the new filename. For example, include the file's creation date, or for image files, the camera model or exposure settings.

<br>

**Search and replace:** A feature to search for files with names that match a certain pattern and replace part of the filename. For example, replace all occurrences of "IMG" with "Image".

<br>

**Recursive renaming:** Add an option to rename files in subdirectories ***_to a certain depth_*** or all the way down.

<br>

**Dry run mode:** You could add a *"dry run"* mode that prints out what changes would be made, without actually renaming any files. This would allow the user to check what the script will do before they run it for real.

<br>

**Undo functionality:** You could keep a record of what changes the script makes, and add an "undo" command to revert the last batch of changes.

<br>

**Improved Logging:** You could add logging to keep a record of what changes the script makes. This could be useful for debugging, or if you want to keep a record of what the script has done.

<br>

---

<br>

## So...

While EZ-Name is currently quite basic, I see a lot of potential for it to grow. I envision adding features like custom separators, metadata-based renaming, recursive renaming, and more. I also see potential for integrating EZ-Name with other tools and workflows, or even developing a GUI for it.

---

<br>

## How can I...

contribute? Sure! EZ-Name is an open-source project, and I welcome contributions from other developers. Whether you have an idea for a new feature, a bug fix, or even just some feedback, I'd love to hear from you. Feel free to open an issue or submit a pull request.

---

<br>

## Details

---

There are no dependencies or libraries at this point. It's just a simple script that you can deploy over a directory with an option to include the files contained with it's sub-driectories.

<br>

To run this program:

<br>

open up your os's terminal and use the `cd` into an appropriate place to store the program.

<br>

<sub>example</sub>

```shell
cd HardDrive/Users/YourUsername/Documents/
```
<br>

clone this repository by copy pasting the following command:

```shell
git clone 
```

<br>

hit enter. navigate into the repository root directory:

```shell
cd EZ-Name
```

<br>


> Note: There are no dependencies at this stage. Just Python 3. So, no need to install a virtual environment or set any variables.

now you can just run the script:

```shell
python3 app.py
```

<br>

In a moment, you'll have to tell the script where the files are that you'd like to rename by providing the path.

before you do that, a message will appear asking if you would like to include files contained within all of the sub-directories as well as the main directory that you specify. 

<br>

If so, typoe:

```shell
RENAME-ALL-FILES
```

then hit `return` or `enter`

<br>

if NOT:

Press any key to continue. This is the default. This will not rename any files contained within any sub folders.

Now enter the path to the absolute path to the folder that contains the files that you'd like to rename.

<br>

using our example from above, assuming your files are in the `Documents` directory you could type this:

```shell
/Users/YourUserName/Documents/FolderWithFilesToRename
```

or in this case, since both the folder and the script are both located in the `Documents` directory you could type:

```shell
../Documents/FolderWithFilesToRename
```

whereby `FolderWithFilesToRename` is the name of your actual folder.

<br>

hit enter.

A message will be printed to the terminal for each action that was taken (the file was either renamed, skipped if not applicable or a copy was created if there was a naming conflict).

---

<br>

## Caution

"Running EZ-Name changes filenames to `kebab-case`. In shell, access files with `cat ./file-name.txt` or `cat "file-name.txt"` to avoid `-` being read as an option specifier."

---

<br>

## License

EZ-Name is licensed under the MIT License. See `LICENSE` for more information.

---
