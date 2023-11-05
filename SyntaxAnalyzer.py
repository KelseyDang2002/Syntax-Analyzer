# Used to exit program gracefully 
import time
import sys

from syntax_rules import *

# define separators, operators and reserved words
separator = [' ', '\t', ',', ';', '(', ')', '{', '}', '#']
operators = ['+', '-', '*', '/', '=', '<', '>', '<=', '=>', '==', '!=', '!']
keyword = ['if', 'else', 'endif' ,'while', 'function', 'integer', 'bool', 'real', 'ret', 'put', 'get', 'true', 'false']
begin_comment = '[*'
end_comment = '*]'

# define array to store all the words that have been read
words = []

# define dictionary to store tokens
tokens = []

# define current line
current_line = 1

# variables for parser
current_token = None
token_index = 0

# variables for output file
output_file = None

switch = False

# *********************************************************************************************************************************
# ******************************SYNTAX ANALYZER CODE STARTS HERE*******************************************************************
# *********************************************************************************************************************************
"""All the rules and functions for the syntax analyzer are here for top down parsing"""
def change_switch():
    global switch
    if switch == False:
        switch = True
    else:
        switch = False

def get_next_token():
    global current_token, token_index
    if token_index < len(tokens):
        current_token = tokens[token_index]
        token_index += 1

def print_token():
    global current_token,  output_file
    if current_token['token'] == 'illegal' or current_token['token'] == 'keyword' or current_token['token'] == 'integer' or current_token['token'] == 'real':
        print(f"{current_token['token']}\t\t\t{current_token['lexeme']}")
        with open(output_file, "a") as file:
            file.write(f"{current_token['token']}\t\t\t{current_token['lexeme']}")
    else:
        print(f"{current_token['token']}\t\t{current_token['lexeme']}")
        with open(output_file, "a") as file:
            file.write(f"{current_token['token']}\t\t{current_token['lexeme']}")

# Rule 1
# R1) <Rat23F> ::= <Opt Function Definitions> # <Opt Declaration List> <Statement List> #
def Rat23F():
    global current_token, switch, output_file
    get_next_token()
    print_token()
    # print rule
    if switch == False:
        print("\t<Rat23F> ::= <Opt Function Definitions> # <Opt Declaration List> <Statement List> #")
        with open(output_file, "a") as file:
            file.write("\t<Rat23F> ::= <Opt Function Definitions> # <Opt Declaration List> <Statement List> #")
    # call first function
    OptFunctionDefinitions()
    if current_token['lexeme'] == '#':
        get_next_token()
        print_token()
        OptDeclarationList()
        StatementList()
        if current_token['lexeme'] == '#':
            get_next_token()
            print_token()
        else:
            print(f"Error: Expected '#' at line {current_token['line']}.")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '#' at line {current_token['line']}.")
    else: 
        print(f"Error: Expected '#' at line {current_token['line']}.")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected '#' at line {current_token['line']}.")


# Rule 2
# R2) <Opt Function Definitions> ::= <Function Definitions> | <Empty>
def OptFunctionDefinitions():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
    FunctionDefinitions()
    Empty()


# Rule 3
# R3) <Function Definitions> ::= <Function> <Function Definitions Prime>
def FunctionDefinitions():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Function Definitions> ::= <Function> <Function Definitions Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Function Definitions> ::= <Function> <Function Definitions Prime>")
    Function()
    FunctionDefinitionsPrime()


# Rule 4
# R4) <Function Definitions Prime> ::= epsilon | <Function Definitions>
def FunctionDefinitionsPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Function Definitions Prime> ::= epsilon | <Function Definitions>")
        with open(output_file, "a") as file:
            file.write("\t<Function Definitions Prime> ::= epsilon | <Function Definitions>")
    Empty()
    FunctionDefinitions()

#Rule 5
# R5) <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
        with open(output_file, "a") as file:
            file.write("\t<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    if current_token['lexeme'] == 'function':
        get_next_token()
        print_token()
        if current_token['token'] == 'identifier':
            get_next_token()
            print_token()
            if current_token['lexeme'] == '(':
                get_next_token()
                print_token()
                OptParameterList()
                if current_token['lexeme'] == ')':
                    get_next_token()
                    print_token()
                    OptDeclarationList()
                    Body()
                else:
                    print(f"Error: Expected ')' at line {current_token['line']}.")
                    with open(output_file, "a") as file:
                        file.write(f"Error: Expected ')' at line {current_token['line']}.")
            else:
                print(f"Error: Expected '(' at line {current_token['line']}.")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected '(' at line {current_token['line']}.")
        else:
            print(f"Error: Expected 'identifier' at line {current_token['line']}.")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected 'identifier' at line {current_token['line']}.")
    else:
        print(f"Error: Expected 'function' keyword at line {current_token['line']}.")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'function' keyword at line {current_token['line']}.")


# *********************************************************************************************************************************
# ******************************SYNTAX ANALYZER CODE ENDS HERE********************************************************************* 
# *********************************************************************************************************************************



# Code to read the file and store its words in an array
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # here we store the current word read
            word = ""
            while True:
                char = file.read(1)
                if not char:
                    break  # End of file, we exit loop
                # TODO: CHECK IF THIS FIXES ISSUE WITH NEWLINES
                # check for new line character
                if char == '\n':
                    if word:
                        words.append(word)
                        word = ""
                    words.append(char)
                # check for comments
                elif char == '[':
                    if word:
                        words.append(word)
                        word = ""
                    # check for correct opening comment
                    next_char = file.read(1)
                    if char + next_char == begin_comment:
                        words.append(char + next_char)
                    else:
                        # store single operator 
                        words.append(char)
                        # check if next character is a separator
                        if next_char in separator:
                            if next_char != ' ' and char != '\n' and char != '\t':
                                words.append(next_char)
                        else:    
                            word += next_char

                elif char in operators: # read operator
                    if word:
                        words.append(word)
                        word = ""
                    # check for double character operators
                    next_char = file.read(1)
                    # check for closing comment
                    if char + next_char == end_comment:
                        words.append(char + next_char)

                    elif char + next_char in operators:
                        words.append(char + next_char)
                    else:
                        # store single operator 
                        words.append(char)
                        # check if next character is a separator
                        if next_char in separator:
                            if next_char != ' ' and char != '\n' and char != '\t':
                                words.append(next_char)
                        # remove next if in case that we want to make this illegal
                        elif next_char in operators:
                            words.append(next_char)
                        else:    
                            word = next_char

                elif char in separator: # read separator
                    if word:
                        words.append(word)
                        word = ""
                    # in case that we dont want to store whitespaces
                    #remove "if" to keep whitespaces
                    if char != ' ' and char != '\t':
                        words.append(char)
                else:
                    word += char
            if word:
                words.append(word)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except PermissionError:
        print(f"You do not have permission to read the file: '{file_name}'.")
    except OSError as systemError:  
        print(f"An error occurred while reading the file: '{file_name}'. The error was: {systemError}")
    except Exception as errorMessage:
        print(f"An unexpected error occurred while reading the file: '{file_name}'. The error was: {str(errorMessage)}")

# finite state machine for real and integer
def FSMReal(lexeme):
    current_state = 1
    for char in lexeme:
        # manage initial state
        # we need this because we can't have a "." as the first character
        if current_state == 1:
            if char.isdigit():
                current_state = 2
            else:
                current_state = 5
        # manage state 2 aka integer before "."
        if current_state == 2:
            if char.isdigit():
                current_state = 2
            elif char == '.':
                current_state = 3
            else:
                current_state = 5
        # manage state 3 aka "."
        elif current_state == 3:
            if char.isdigit():
                current_state = 4
            else:
                current_state = 5
        # manage state 4 aka integer after "."
        elif current_state == 4:
            if char.isdigit():
                current_state = 4
            else:
                current_state = 5

    # if our final state is 4, then we have a real
    if current_state == 4:
        # store token and lexeme
        tokens.append({'token': 'real', 'lexeme': lexeme, 'line': current_line})
    # if our final state is 2, then we have an integer
    elif current_state == 2:
        tokens.append({'token': 'integer', 'lexeme': lexeme, 'line': current_line})
    # in case of failure
    else:
        tokens.append({'token': 'illegal', 'lexeme': lexeme, 'line': current_line})

# finite state machine for identifiers
def FSMIdentifier(identifier):
    current_state = 1
    if len(identifier) == 1:
        if identifier.isalpha():
            tokens.append({'token': 'identifier', 'lexeme': identifier, 'line': current_line})
    else:
        for char in identifier:
            # check if the first character is a letter
            if current_state == 1:
                if char.isalpha():
                    current_state = 2
                else:
                    current_state = 4
            # now we can accept digits and letters
            elif current_state == 2:
                if char.isalpha():
                    # we stay in the same state if letter
                    current_state = 2
                elif char.isdigit():
                    # we move to state 3 if digit
                    current_state = 3
                else:
                    current_state = 4
            # still accepting digits and letters
            elif current_state == 3:
                if char.isalpha():
                    # we go back to state 2 if letter
                    current_state = 2
                elif char.isdigit():
                    # we stay in the same state if digit
                    current_state = 3
                else:
                    current_state = 4
        # final state must be 2 because we need to end in a letter
        if current_state == 2:
            tokens.append({'token': 'identifier', 'lexeme': identifier, 'line': current_line})
        else:
            tokens.append({'token': 'illegal', 'lexeme': identifier, 'line': current_line})

# this is the main lexer function, it is in charge of identifying the tokens
def lexer(word):
    if word in keyword:
        tokens.append({'token': 'keyword', 'lexeme': word, 'line': current_line})
    elif word in operators:
        # check that word is not the only illegal operator "!", only in list for "!="
        if word == '!':
            tokens.append({'token': 'illegal', 'lexeme': word, 'line': current_line})
        else:
            tokens.append({'token': 'operator', 'lexeme': word, 'line': current_line})
    elif word in separator:
        tokens.append({'token': 'separator', 'lexeme': word, 'line': current_line})
    # check if it is a real or an integer
    elif word[0].isdigit():
        FSMReal(word)
    # check if is in an identifier
    elif word[0].isalpha():
        FSMIdentifier(word)
    else:
        tokens.append({'token': 'illegal', 'lexeme': word, 'line': current_line})

# this functions removes comments from the code
def commentRemoval(words):
    global current_line
    # keep track if we are in a comment 
    comment = False
    # iterate through lexemes 
    for word in words:
        if word == "\n":
            current_line += 1
            print(f"Current line: {current_line}")
        elif word == begin_comment:
            comment = True
        elif comment == False:
            lexer(word)
        elif word == end_comment:
            comment = False

# this functions prints all the tokens to the main program console
def print_tokens(tokens):
    print("token\t\t\tlexeme\t\t\tline")
    print("_________________________________\n")
    for token in tokens:
        if token['token'] == 'illegal' or token['token'] == 'keyword' or token['token'] == 'integer' or token['token'] == 'real':
            print(f"{token['token']}\t\t\t{token['lexeme']}\t\t\t{token['line']}")
        else:
            print(f"{token['token']}\t\t{token['lexeme']}\t\t\t{token['line']}")

# this function generates a file name for the tokens file
def file_name_generator(file_name):
    return 'output_' + file_name

# this function writes all the tokens and lexemes to a file
def write_tokens(tokens):
    global output_file
    try:
        with open(output_file, 'w') as file:
            print(f"\nWriting tokens to file '{output_file}'...\n")
            file.write("token\t\t\tlexeme\t\t\tline\n")
            file.write("_________________________________\n")
            for token in tokens:
                if token['token'] == 'illegal' or token['token'] == 'keyword' or token['token'] == 'integer' or token['token'] == 'real':
                    file.write(f"{token['token']}\t\t\t{token['lexeme']}\t\t\t{token['line']}\n")
                else:
                    file.write(f"{token['token']}\t\t{token['lexeme']}\t\t\t{token['line']}\n")
            print(f"Tokens written to file '{output_file}' successfully!\n")
    except FileNotFoundError:
        print(f"The file '{output_file}' was not found.")
    except PermissionError:
        print(f"You do not have permission to create the file: '{output_file}'.")
    except OSError as systemError:  
        print(f"An error occurred while creating the file: '{output_file}'. The error was: {systemError}")
    except Exception as errorMessage:
        print(f"An unexpected error occurred while creating the file: '{output_file}'. The error was: {str(errorMessage)}")

# Function to analyze a file
def analyze_file():
    global current_line, output_file
    while True:
        try:
            file_name = input("Please enter the name of the file you want to analyze (or 'q' to quit): ")
            if file_name == 'q':
                print("\nThank you for using our Lexical Analyzer!\n")
                print("Exiting program...")
                time.sleep(2)
                sys.exit(0) # Exit the loop and quit the program
            with open(file_name, 'r') as file:
                # The file exists, so continue with analysis
                # create output file name
                output_file = file_name_generator(file_name)
                # clear file in case that there was a previous analysis
                with open(output_file, "w") as file:
                    file.write("")  # This will clear the file's contents
                print(f"\nAnalyzing file '{file_name}'...\n")
                words.clear()  # Clear the list of words from previous analyses
                tokens.clear()  # Clear the list of tokens from previous analyses
                current_line = 1  # Reset the current line to 1
                read_file(file_name)
                commentRemoval(words)
                # TODO: remove print_tokens(tokens) and write_tokens(tokens) before submitting
                print_tokens(tokens)
                write_tokens(tokens)
                # TODO: add rat23f() call here
                # Rat23F()
                break
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found. Please enter a valid file name.")
        except PermissionError:
            print(f"You do not have permission to read the file: '{file_name}'. Please enter a different file name.")
        except Exception as errorMessage:
            print(f"An unexpected error occurred: {str(errorMessage)} Please enter a different file name.")

def main():
    # User interface
    print("\nWelcome to our Syntax Analyzer!")

    # call main function to analyze a file 
    analyze_file()
    # Main loop
    while True:
        another_analysis = input("Do you want to analyze another file? (yes/no): ").strip().lower()
        if another_analysis == 'no' or another_analysis == 'n':
            print("\nThank you for using our Syntax Analyzer!\n")
            print("Exiting program...")
            time.sleep(2)
            sys.exit(0)  # Exit the program if the user does not want to analyze another file
        elif another_analysis == 'yes' or another_analysis == 'y':
            analyze_file()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
