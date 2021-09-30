"""
Problem:
We're going to build the beginnings of a markdown processor. Markdown is a markup language that allows you to easily create HTML.
We ll provide some sample input and desired output. Dont worry too much about edge cases, but feel free to ask if you re unsure or think there s something we ought to consider.

Part 1:  A markdown processor is capable of handling a multitude of string to html tag formats. For now, we just want to focus on supporting <p/>, <br/>, <blockquote/>, and <del/> tags.

Input:
String input = "This is a paragraph with a soft\n" + "line break.\n\n" + "This is another paragraph that has\n" +
               "> Some text that\n" + "> is in a\n" + "> block quote.\n\n" +
			   "This is another paragraph with a ~~strikethrough~~ word.";

Expected Output:
"<p>This is a paragraph with a soft<br />line break.</p>
<p>This is another paragraph that has <br />
<blockquote.>Some text that<br />is in a<b.r />
block quote</blockquote.> </p> <p>This is another paragraph with a
<del>strikethrough</del.> word.</p>"

"""


class SamsaraSolution:
    def markdown(input: str) -> str:
        res = "<p>"
        input = input.replace("\n", "--")

        is_new_para, block_is_active, strikethrough_began = True, False, False
        i = 0
        while i < len(input):
            ch = input[i:i+2] # the first two characters, e.g. "\n", "> ", "~~"

            if ch == '--':
                if input[i+2:i+4] == "--":
                    if block_is_active:
                        res += "</blockquote.>"
                        block_is_active = False
                    res += "</p>"
                    res += "<p>"
                    i += 4
                else:
                    res += "<br />"
                    i += 2
            elif ch == "> ":
                if not block_is_active:
                    res += "<blockquote.>"
                    block_is_active = True
                i += 2
            elif ch == "~~":
                if not strikethrough_began:
                    res += "<del>"
                    strikethrough_began = True
                else:
                    res += "</del>"
                i += 2
            else:
                res += input[i]
                i += 1
        res += "</p>"
        return res

    if __name__ == "__main__":
        input = "This is a paragraph with a soft\nline break.\n\nThis is another paragraph that has\n> Some text that\n> is in a\n> block quote.\n\nThis is another paragraph with a ~~strikethrough~~ word."

        output = markdown(input)
        print("--------input-------------\n", input, "\n-----------------")
        print("--------output-------------\n", output, "\n-----------------")
