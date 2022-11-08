'''
2022 © MaoHuPi
penanaBot/main.py
'''

import os, sys
import json
import tkinter as tk
from PIL import Image, ImageTk
from script import penaBot as bot

path = '.' if os.path.isfile('./'+os.path.basename(__file__)) else os.path.dirname(os.path.abspath(__file__))

accounts = []
elements = []
originalWidth, originalHeight = [480, 270]
fontSize = 10
backgroundColor = '#fff'
frontgroundColor = '#000'

def writeAccount():
    global accounts
    content = json.dumps({'accounts': accounts})
    file = open(path + '/data/account.json', 'w+', encoding = 'utf-8')
    file.write(content)
    file.close()

def readAccount():
    global accounts
    file = open(path + '/data/account.json', 'r+', encoding = 'utf-8')
    content = file.read()
    file.close()
    accounts = json.loads(content)['accounts']

def inputGroup(parent, inputType, text, x, y):
    global fontSize, backgroundColor, frontgroundColor
    lableElement = tk.Label(
        parent, 
        text = text, 
        font = ('Arial', fontSize), 
        anchor = 'w', 
        fg = frontgroundColor, 
        bg = backgroundColor
    )
    lableElement.grid(row = y, column = x)
    inputElement = getattr(tk, inputType)(
        parent, 
        font = ('Arial', fontSize), 
        fg = frontgroundColor, 
        bg = backgroundColor
    )
    inputElement.grid(row = y, column = x + 1)
    elements.append(lableElement)
    elements.append(inputElement)
    return([lableElement, inputElement])

def buttonGroup(parent, texts, x, y):
    global fontSize, backgroundColor, frontgroundColor
    buttons = []
    frameElement = tk.Frame(parent)
    frameElement.grid(row = y, column = x, columnspan = 2)
    for text in texts:
        buttonElement = tk.Button(
            frameElement, 
            text = text, 
            font = ('Arial', fontSize), 
            anchor = 'w', 
            fg = frontgroundColor, 
            bg = backgroundColor
        )
        buttonElement.grid(row = 0, column = len(buttons))
        buttons.append(buttonElement)
        elements.append(buttonElement)
    return(buttons)

def main():
    global url, fontSize, accounts, backgroundColor, frontgroundColor
    url = 'https://www.penana.com'

    root = tk.Tk()
    root.title('Pena Bot Interface')
    root.geometry('{width}x{height}'.format(width = originalWidth, height = originalHeight))
    # root.resizable(width=0, height=0)
    root['bg'] = backgroundColor
    # root.wm_attributes('-transparentcolor', root['bg'])
    run = True

    readAccount()

    def rootResize():
        global fontSize
        fontSize += 5
        width = originalWidth/10*fontSize
        height = originalHeight/10*fontSize
        root.geometry('{width}x{height}'.format(width = int(width), height = int(height)))

        middleFrame.config(height = int(height - fontSize*4*2))
        middleFrame.coords('middleLine', 5, 10, 5, int(height - fontSize*4*2 - 10))

        bearSize = int(100/10*fontSize)
        bear = Image.open(path + '/image/penaBot.png')
        bear = bear.resize((bearSize, bearSize), Image.ANTIALIAS)
        bear = ImageTk.PhotoImage(bear)
        bearImage.config(image = bear)

    title = tk.Label(
        root, 
        text = 'Pena Bot', 
        font = ('Arial', fontSize*2), 
        anchor = 'center', 
        fg = frontgroundColor, 
        bg = backgroundColor, 
        height = 2
    )
    title.grid(row = 0, column = 0, columnspan = 5)
    elements.append(title)

    leftPadding = tk.Frame(
        root, 
        width = 10, 
        bg = backgroundColor
    )
    leftPadding.grid(row = 1, column = 0)

    leftFrame = tk.Frame(
        root, 
        bg = backgroundColor
    )
    leftFrame.grid(row = 1, column = 1)
    [accountLable, accountEntry] = inputGroup(leftFrame, 'Entry', 'Account', x = 0, y = 0)
    [passwordLable, passwordEntry] = inputGroup(leftFrame, 'Entry', 'Password', x = 0, y = 1)
    [loginButton, logoutButton] = buttonGroup(leftFrame, ['Login', 'Logout'], x = 0, y = 2)
    
    bear = Image.open(path + '/image/penaBot.png')
    bear = bear.resize((100, 100), Image.ANTIALIAS)
    bear = ImageTk.PhotoImage(bear)
    bearImage = tk.Label(
        leftFrame, 
        bg = backgroundColor, 
        image = bear
    )
    bearImage.grid(row = 3, column = 0, columnspan = 2)

    middleFrame = tk.Canvas(
        root, 
        width = 10, 
        height = 200, 
        bg = backgroundColor, 
        bd = 0, 
        highlightthickness = 0
    )
    middleFrame.grid(row = 1, column = 2)
    middleLine = middleFrame.create_line(5, 10, 5, 190, dash=(4, 2), tags = 'middleLine')
    rootResize()
    
    rightFrame = tk.Frame(
        root, 
        bg = backgroundColor
    )
    rightFrame.grid(row = 1, column = 3)
    [targetLable, targetEntry] = inputGroup(rightFrame, 'Entry', 'Target', x = 0, y = 0)
    [typeLable, typeEntry] = inputGroup(rightFrame, 'Entry', 'Type', x = 0, y = 1)
    [penaCoinLable, penaCoinEntry] = inputGroup(rightFrame, 'Entry', 'Pena Coin', x = 0, y = 2)
    [coinPoolLable, coinPoolEntry] = inputGroup(rightFrame, 'Entry', 'Coin Pool', x = 0, y = 3)
    [msgContentLable, msgContentEntry] = inputGroup(rightFrame, 'Entry', 'Msg Content', x = 0, y = 4)
    [targetAccountLable, targetAccountEntry] = inputGroup(rightFrame, 'Entry', 'Target Account', x = 0, y = 5)
    [targetStoryLable, targetStoryEntry] = inputGroup(rightFrame, 'Entry', 'Target Story', x = 0, y = 6)
    [submitButton] = buttonGroup(rightFrame, ['Submit'], x = 0, y = 7)

    rightPadding = tk.Frame(
        root, 
        width = 10, 
        bg = backgroundColor
    )
    rightPadding.grid(row = 1, column = 4)

    account = accounts[0]['account']
    password = accounts[0]['password']

    # cookie = bot.login(account, password)
    print(account, password)
    # bot.like(cookie, 114674, 2)
    while run:
        root.update()

if __name__ == '__main__':
    main()