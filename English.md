# Transparent file suffix script

## Introduction

This Python script is used to change the suffix of a file in a specified directory to include invisible characters (effective in Windows), thus making the file suffix transparent in the file Explorer. This can be useful for hiding certain types of files or creating visually suffix-free files.

## How to use

1. Run this script in the Windows environment where the file you want to manipulate is located (run in administrator mode).
2. When you run the script, it will prompt you to enter the file suffix you want to make transparent. For example, you can type '.lnk 'to make all shortcut suffixes transparent, or enter nothing to apply to a folder.
3. After the input is complete, the script traverses the current directory and renames all files that match the specified suffix.
4. Add a transparent character before the suffix of the modified file name. Each iteration of this character will increase one character to ensure the uniqueness of the file name.

Please note: This script has been tested under Windows and has not been verified for Linux.

## Precautions

- ** Data security ** : Before using this script, make sure you have backed up important data, as a wrong operation may cause files not to be accessed correctly.
- ** Permission issues ** : If the file is in a location that requires administrator permission to modify, make sure to run the script as administrator.
- ** File Recovery ** : Once a file has been renamed, restoring the original name may require manual action, or writing another script to reverse the change.
- ** Transparent character ** : The transparent character used (' ') is a special space character that may behave differently in different operating systems and applications.
- ** Restart the computer ** : Restart the computer or terminate the window manager to refresh the desktop resources if it does not take effect.

* Last updated: January 23, 2025 *

---
