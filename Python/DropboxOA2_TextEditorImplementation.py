'''
Text Editor Implementation
A text editor is a type of computer program that edits plain text.

Your task is to simulate the working process of a text editor which can handle five types of operations:

    INSERT <text> - add <text> to the end of the current text, where <text> consists of at most 20 English letters,
	
    DELETE - erase the last character of the current text (if the current text is empty, does nothing),
	
    COPY <index> - copy the substring of the current text starting from <index> and spanning until the end (if <index> is out of bounds copies an empty string), i.e. sets the clipboard value equal to the given substring,
	
    PASTE - add the last copied text to the end of the current text (if the last copied text is empty, does nothing),
	
    UNDO - undo the last successful INSERT, DELETE or PASTE operation (if there is nothing to undo, does nothing).

     For operations = ["INSERT Da", "COPY 0", "UNDO", "PASTE", "PASTE", "COPY 2", "PASTE", "PASTE", "DELETE", "INSERT aaam"], the output should be newTextEditor(operations) = "DaDaDaDaaam".
	
        Initially the text is empty,
		
        After the "INSERT Da" operation, the text is "Da",
		
        After the "COPY 0" operation, the clipboard is set to "Da", the text is left unchanged,
		
        After the "UNDO" operation, the INSERT operation is undone, so the text is "",
		
        After the "PASTE" operation, the text "Da" is inserted from the clipboard, so the editor text is changed to "Da",
		
        After the "PASTE" operation, the text "Da" is inserted from the clipboard, so the editor text is changed to "DaDa",
		
        After the "COPY 2" operation, the clipboard is set to "Da", the editor text is left unchanged,
		
        After the "PASTE" operation, the text "Da" is inserted, so the editor text is changed to "DaDaDa",
		
        After the "PASTE" operation, the text "Da" is inserted, so the editor text is changed to "DaDaDaDa",
		
        After the "DELETE" operation, the last character is removed, so the text is "DaDaDaD",
		
        After the "INSERT aaam" operation, the text is "DaDaDaDaaam",
		
        So the final editor text is "DaDaDaDaaam".

Input/Output

    [execution time limit] 0.5 seconds (cpp)

    [input] array.string operations

    A sequence of operations. It's guaranteed that all the operations satisfy the format described in the description.

    Guaranteed constraints:
    1 ≤ operations.length ≤ 103.

    [output] string

    The resulting text after performing the given sequence of operations.

'''

import collections
from typing import Text

class TextEditor:
    def __init__(self) -> None:
        self._text = "" # store the latest version of text until now
        self.stack = collections.deque()
        self.clipboard = "" # 

    def insert(self, text) -> None:
        # add text to the end of the current text 
        # in case we need to undo the insert, we store the len(text)
        self.stack.append(['i', len(text)])
        self._text += text
    
    def copy(self, index) -> None:
        '''
        copy the substring of the current text starting from <index> and spanning until the end (if <index> is out of bounds copies an empty string), i.e. sets the clipboard value equal to the given substring
        '''
        if index > len(self._text) or index < 0:
            return
        self.clipboard = self._text[index:]
    
    def delete(self) -> None:
        # erase the last character of the current text 
        # #(if the current text is empty, does nothing)
        if self._text is None:
            return
        self.stack.append(['d', self._text[-1]])
        self._text = self._text[:-1]
    
    def paste(self) -> None:
        # add the last copied text to the end of the current text 
        # (if the last copied text is empty, does nothing),
        self.insert(self.clipboard)

    def undo(self) -> None:
        # undo the last successful INSERT, DELETE or PASTE operation 
        # (if there is nothing to undo, does nothing).
        if self.stack:
            op, detail = self.stack.pop()
            if op == 'i':
                # remove the inserted text
                self._text = self._text[:len(self._text) - detail]
            elif op == 'd':
                # place back the last deleted character to the end
                self._text += detail
    
    def text(self):
        return self._text

if __name__ == '__main__':
    # For operations = ["INSERT Da", "COPY 0", "UNDO", "PASTE", "PASTE", "COPY 2", "PASTE", "PASTE", "DELETE", "INSERT aaam"], 
    # the output should be newTextEditor(operations) = "DaDaDaDaaam".

    ted = TextEditor()

    ted.insert("Da")
    ted.copy(0)
    ted.undo()
    ted.paste()
    ted.paste()
    ted.copy(2)
    ted.paste()
    ted.paste()
    ted.delete()
    ted.insert("aaam")
    print(ted.text())
    if ted.text() == 'DaDaDaDaaam':
        print('pass')
    else:
        print('error!')
