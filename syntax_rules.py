# switch function to turn on/off print syntax rules
def Switch():
    # todo
    print("Switch")

# Rule 1
def Rat23F():
    # todo
    print("<Rat23F> -> <Opt Function Definitions> # <Opt Declaration List> <Statement List> #")

# Rule 2
def OptFunctionDefinitions():
    # todo
    print("<Opt Function Definitions> -> <Function Definitions>")
    # todo
    print("<Opt Function Definitions> -> epsilon")

# Rule 3
def FunctionDefinitions():
    # todo
    print("<Function Definitions> -> <Function> <Function Definitions Prime>")

# Rule 4
def FunctionDefinitionsPrime():
    # todo
    print("<Function Definitions Prime> -> <Function Definitions>")
    # todo
    print("<Function Definitions Prime> -> epsilon")

# Rule 5
def Function():
    # todo
    print("<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")

# Rule 6
def OptParameterList():
    # todo
    print("<Opt Parameter List> -> <Parameter List>")
    # todo
    print("<Opt Parameter List> -> <Empty>")

# Rule 7
def ParameterList():
    # todo
    print("<Parameter List> -> <Parameter> <Parameter List Prime>")

# Rule 8
def ParameterListPrime():
    # todo
    print("<Parameter List Prime> -> , <Parameter List>")
    # todo
    print("<Parameter List Prime> -> epsilon")

# Rule 9
def Parameter():
    # todo
    print("<Parameter> -> <IDs> <Qualifier>")

# Rule 10
def Qualifier():
    # todo
    print("<Qualifier> -> integer")
    # todo
    print("<Qualifier> -> bool")
    # todo
    print("<Qualifier> -> real")

# Rule 11
def Body():
    # todo
    print("<Body> -> { <Statement List> }")

# Rule 12
def OptDeclarationList():
    # todo
    print("<Opt Declaration List> -> <Declaration List>")
    # todo
    print("<Opt Declaration List> -> <Empty>")

# Rule 13
def DeclarationList():
    # todo
    print("<Declaration List> -> <Declaration> ; <Declaration List Prime>")

# Rule 14
def DeclarationListPrime():
    # todo
    print("<Declaration List Prime> -> <Declaration List>")
    # todo
    print("<Declaration List Prime> -> epsilon")

# Rule 15
def Declaration():
    # todo
    print("<Declaration> -> <Qualifier> <IDs>")

# Rule 16
def IDs():
    # todo
    print("<IDs> -> <Identifier> <IDs Prime>")

# Rule 17
def IDsPrime():
    # todo
    print("<IDs Prime> -> , <IDs>")
    # todo
    print("<IDs Prime> -> epsilon")

# Rule 18
def StatementList():
    # todo
    print("<Statement List> -> <Statement> <Statement List Prime>")

# Rule 19
def StatementListPrime():
    # todo
    print("<Statement List Prime> -> <Statement List>")
    # todo
    print("<Statement List Prime> -> epsilon")

# Rule 20
def Statement():
    # todo
    print("<Statement> -> <Compound>")
    # todo
    print("<Statement> -> <Assign>")
    # todo
    print("<Statement> -> <If>")
    # todo
    print("<Statement> -> <Return>")
    # todo
    print("<Statement> -> <Print>")
    # todo
    print("<Statement> -> <Scan>")
    # todo
    print("<Statement> -> <While>")

# Rule 21
def Compound():
    # todo
    print("<Compound> -> { <Statement List> }")

# Rule 22
def Assign():
    # todo
    print("<Assign> -> <Identifier> = <Expression> ;")

# Rule 23
def If():
    # todo
    print("<If> -> if ( <Condition> ) <Statement> <If Prime>")

# Rule 24
def IfPrime():
    # todo
    print("<If Prime> -> endif")
    # todo
    print("<If Prime> -> else <Statement> endif")

# Rule 25
def Return():
    # todo
    print("<Return> -> ret <Return Prime>")

# Rule 26
def ReturnPrime():
    # todo
    print("<Return Prime> -> ;")
    # todo
    print("<Return Prime> -> <Expression> ;")

# Rule 27
def Print():
    # todo
    print("<Print> -> put ( <Expression> );")

# Rule 28
def Scan():
    # todo
    print("<Scan> -> get ( <IDs> );")

# Rule 29
def While():
    # todo
    print("<While> -> while ( <Condition> ) <Statement>")

# Rule 30
def Condition():
    # todo
    print("<Condition> -> <Expression> <Relop> <Expression>")

# Rule 31
def Relop():
    # todo
    print("<Relop> -> ==")
    # todo
    print("<Relop> -> !=")
    # todo
    print("<Relop> -> >")
    # todo
    print("<Relop> -> <")
    # todo
    print("<Relop> -> <=")
    # todo
    print("<Relop> -> =>")

# Rule 32
def Expression():
    # todo
    print("<Expression> -> <Term> <Expression Prime>")

# Rule 33
def ExpressionPrime():
    # todo
    print("<Expression Prime> -> + <Term> <Expression Prime>")
    # todo
    print("<Expression Prime> -> - <Term> <Expression Prime>")
    # todo
    print("<Expression Prime> -> epsilon")

# Rule 34
def Term():
    # todo
    print("<Term> -> <Factor> <Term Prime>")

# Rule 35
def TermPrime():
    # todo
    print("<Term Prime> -> * <Factor> <Term Prime>")
    # todo
    print("<Term Prime> -> / <Factor> <Term Prime>")
    # todo
    print("<Term Prime> -> epsilon")

# Rule 36
def Factor():
    # todo
    print("<Factor> -> - <Primary>")
    # todo
    print("<Factor> -> <Primary>")

# Rule 37
def Primary():
    # todo
    print("<Primary> -> <Identifier> <Primary Prime>")
    # todo
    print("<Primary> -> <Integer>")
    # todo
    print("<Primary> -> ( <Expression> )")
    # todo
    print("<Primary> -> <Real>")
    # todo
    print("<Primary> -> true")
    # todo
    print("<Primary> -> false")

# Rule 38
def PrimaryPrime():
    # todo
    print("<Primary Prime> -> ( <IDs> )")
    # todo
    print("<Primary Prime> -> epsilon")

# Rule 39
def Empty():
    # does nothing
    print("<Empty> -> epsilon")