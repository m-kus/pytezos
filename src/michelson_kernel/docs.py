docs = {
    'ABS': 'ABS\nABS :: int : A => nat : A\nObtain the absolute value of an integer',
    'ADD': 'ADD\n'
           'ADD :: nat : nat : A => nat : A\n'
           'ADD :: nat : int : A => int : A\n'
           'ADD :: int : nat : A => int : A\n'
           'ADD :: int : int : A => int : A\n'
           'ADD :: timestamp : int : A => timestamp : A\n'
           'ADD :: int : timestamp : A => timestamp : A\n'
           'ADD :: mutez : mutez : A => mutez : A\n'
           'Add two numerical values',
    'ADDRESS': 'ADDRESS\nADDRESS :: contract ty1 : A => address : A\nPush the address of a contract',
    'AMOUNT': 'AMOUNT\nAMOUNT :: A => mutez : A\nPush the amount of the current transaction',
    'AND': 'AND\nAND :: bool : bool : A => bool : A\nAND :: nat : nat : A => nat : A\nBoolean and bitwise AND',
    'APPLY': 'APPLY\n'
             'APPLY :: ty1 : lambda ( pair ty1 ty2 ) ty3 : A => lambda ty2 ty3 : A\n'
             'Partially apply a tuplified function from the stack',
    'BALANCE': 'BALANCE\nBALANCE :: A => mutez : A\nPush the current amount of mutez of the executing contract',
    'BLAKE2B': 'BLAKE2B\nBLAKE2B :: bytes : A => bytes : A\nCompute a Blake2B cryptographic hash',
    'CAR': 'CAR\nCAR :: pair ty1 ty2 : A => ty1 : A\nAccess the left part of a pair',
    'CAST': '',
    'CDR': 'CDR\nCDR :: pair ty1 ty2 : A => ty2 : A\nAccess the right part of a pair',
    'CHAIN_ID': 'CHAIN_ID\nCHAIN_ID :: A => chain_id : A\nPush the chain identifier',
    'CHECK_SIGNATURE': 'CHECK_SIGNATURE\n'
                       'CHECK_SIGNATURE :: key : signature : bytes : A => bool : A\n'
                       'Verify signature of bytes by key',
    'COMPARE': 'COMPARE\nCOMPARE :: cty : cty : A => int : A\nCompare two values',
    'CONCAT': 'CONCAT\n'
              'CONCAT :: string : string : A => string : A\n'
              'CONCAT :: list string : A => string : A\n'
              'CONCAT :: bytes : bytes : A => bytes : A\n'
              'CONCAT :: list bytes : A => bytes : A\n'
              'Concatenate a string, byte sequence, string list or byte sequence list',
    'CONS': 'CONS\nCONS :: ty1 : list ty1 : A => list ty1 : A\nPrepend an element to a list',
    'CONTRACT': 'CONTRACT ty\n'
                'CONTRACT ty1 :: address : A => option ( contract ty1 ) : A\n'
                'Cast an address to a typed contract',
    'CREATE_ACCOUNT': '\nPush an account creation operation',
    'CREATE_CONTRACT': 'CREATE_CONTRACT ty1 ty2 code\n'
                       'CREATE_CONTRACT ty1 ty2 code :: option key_hash : mutez : ty1 : A => operation : address : A\n'
                       'Push a contract creation operation',
    'DIG': 'DIG n\nDIG n :: A @ ( ty1 : B ) => ty1 : ( A @ B )\nRetrieve the n\\ th element of the stack',
    'DIP': 'DIP n code\nDIP n code :: A @ B => A @ C\nRun code protecting the top of the stack',
    'DROP': 'DROP n\nDROP n :: A @ B => B\nDrop the top n elements of the stack',
    'DUG': 'DUG n\nDUG n :: ty1 : ( A @ B ) => A @ ( ty1 : B )\nInsert the top element at depth n',
    'DUP': 'DUP\nDUP :: ty1 : A => ty1 : ty1 : A\nDuplicate the top of the stack',
    'EDIV': 'EDIV\n'
            'EDIV :: nat : nat : A => option ( pair nat nat ) : A\n'
            'EDIV :: nat : int : A => option ( pair int nat ) : A\n'
            'EDIV :: int : nat : A => option ( pair int nat ) : A\n'
            'EDIV :: int : int : A => option ( pair int nat ) : A\n'
            'EDIV :: mutez : nat : A => option ( pair mutez mutez ) : A\n'
            'EDIV :: mutez : mutez : A => option ( pair nat mutez ) : A\n'
            'Euclidean division',
    'EMPTY_BIG_MAP': 'EMPTY_BIG_MAP kty vty\n'
                     'EMPTY_BIG_MAP kty vty :: A => big_map kty vty : A\n'
                     'Build a new, empty big_map from kty to vty',
    'EMPTY_MAP': 'EMPTY_MAP kty vty\nEMPTY_MAP kty vty :: A => map kty vty : A\nBuild a new, empty map from kty to vty',
    'EMPTY_SET': 'EMPTY_SET cty\nEMPTY_SET cty :: A => set cty : A\nBuild a new, empty set for elements of type cty',
    'EQ': 'EQ\nEQ :: int : A => bool : A\nCheck that the top of the stack EQuals zero',
    'EXEC': 'EXEC\nEXEC :: ty1 : lambda ty1 ty2 : A => ty2 : A\nExecute a function from the stack',
    'EXPAND': '',
    'FAILWITH': 'FAILWITH\nFAILWITH :: ty1 : A => B\nExplicitly abort the current program',
    'GE': 'GE\nGE :: int : A => bool : A\nCheck that the top of the stack is Greater Than or Equal to zero',
    'GET': 'GET\n'
           'GET :: kty : map kty vty : A => option vty : A\n'
           'GET :: kty : big_map kty vty : A => option vty : A\n'
           'Access an element in a map or big_map',
    'GT': 'GT\nGT :: int : A => bool : A\nCheck that the top of the stack is Greater Than zero',
    'HASH_KEY': 'HASH_KEY\nHASH_KEY :: key : A => key_hash : A\nCompute the Base58Check of a public key',
    'IF': 'IF code1 code2\nIF code1 code2 :: bool : A => B\nConditional branching',
    'IF_CONS': 'IF_CONS code1 code2\nIF_CONS code1 code2 :: list ty1 : A => B\nInspect a list',
    'IF_LEFT': 'IF_LEFT code1 code2\nIF_LEFT code1 code2 :: or ty1 ty2 : A => B\nInspect a value of a union',
    'IF_NONE': 'IF_NONE code1 code2\nIF_NONE code1 code2 :: option ty1 : A => B\nInspect an optional value',
    'IMPLICIT_ACCOUNT': 'IMPLICIT_ACCOUNT\n'
                        'IMPLICIT_ACCOUNT :: key_hash : A => contract unit : A\n'
                        'Create an implicit account',
    'INT': 'INT\nINT :: nat : A => int : A\nConvert a natural number to an integer',
    'ISNAT': 'ISNAT\nISNAT :: int : A => option nat : A\nConvert a non-negative integer to a natural number',
    'ITER': 'ITER code\n'
            'ITER code :: list ty1 : A => A\n'
            'ITER code :: set cty : A => A\n'
            'ITER code :: map kty vty : A => A\n'
            'Iterate over a set, list or map',
    'LAMBDA': 'LAMBDA ty1 ty2 code\nLAMBDA ty1 ty2 code :: A => lambda ty1 ty2 : A\nPush a lambda onto the stack',
    'LE': 'LE\nLE :: int : A => bool : A\nCheck that the top of the stack is Less Than or Equal to zero',
    'LEFT': 'LEFT ty2\nLEFT ty2 :: ty1 : A => or ty1 ty2 : A\nWrap a value in a union (left case)',
    'LOOP': 'LOOP code\nLOOP code :: bool : A => A\nA generic loop',
    'LOOP_LEFT': 'LOOP_LEFT code\nLOOP_LEFT code :: or ty1 ty2 : A => ty2 : A\nLoop with accumulator',
    'LSL': 'LSL\nLSL :: nat : nat : A => nat : A\nLogically left shift a natural number',
    'LSR': 'LSR\nLSR :: nat : nat : A => nat : A\nLogically right shift a natural number',
    'LT': 'LT\nLT :: int : A => bool : A\nCheck that the top of the stack is Less Than zero',
    'MAP': 'MAP code\n'
           'MAP code :: list ty1 : A => list ty2 : A\n'
           'MAP code :: map kty ty1 : A => map kty ty2 : A\n'
           'Apply the body expression to each element of a list or map.',
    'MEM': 'MEM\n'
           'MEM :: cty : set cty : A => bool : A\n'
           'MEM :: kty : map kty vty : A => bool : A\n'
           'MEM :: kty : big_map kty vty : A => bool : A\n'
           'Check for the presence of a binding for a key in a map, set or big_map',
    'MUL': 'MUL\n'
           'MUL :: nat : nat : A => nat : A\n'
           'MUL :: nat : int : A => int : A\n'
           'MUL :: int : nat : A => int : A\n'
           'MUL :: int : int : A => int : A\n'
           'MUL :: mutez : nat : A => mutez : A\n'
           'MUL :: nat : mutez : A => mutez : A\n'
           'Multiply two numerical values',
    'NEG': 'NEG\nNEG :: nat : A => int : A\nNEG :: int : A => int : A\nNegate a numerical value',
    'NEQ': 'NEQ\nNEQ :: int : A => bool : A\nCheck that the top of the stack does Not EQual zero',
    'NIL': 'NIL ty1\nNIL ty1 :: A => list ty1 : A\nPush an empty list',
    'NONE': 'NONE ty1\nNONE ty1 :: A => option ty1 : A\nPush the absent optional value',
    'NOOP': '{}\n{} :: A => A\nEmpty instruction sequence',
    'NOT': 'NOT\n'
           'NOT :: bool : A => bool : A\n'
           'NOT :: nat : A => int : A\n'
           'NOT :: int : A => int : A\n'
           'Boolean negation and bitwise complement',
    'NOW': 'NOW\nNOW :: A => timestamp : A\nPush block timestamp',
    'OR': 'OR\nOR :: bool : bool : A => bool : A\nOR :: nat : nat : A => nat : A\nBoolean and bitwise OR',
    'PACK': 'PACK\nPACK :: ty1 : A => bytes : A\nSerialize data',
    'PAIR': "PAIR\nPAIR :: ty1 : ty2 : A => pair ty1 ty2 : A\nBuild a pair from the stack's top two elements",
    'PUSH': 'PUSH ty1 x\nPUSH ty1 x :: A => ty1 : A\nPush a constant value of a given type onto the stack',
    'RENAME': '',
    'RIGHT': 'RIGHT ty1\nRIGHT ty1 :: ty2 : A => or ty1 ty2 : A\nWrap a value in a union (right case)',
    'SELF': 'SELF\nSELF :: A => contract ty : A\nPush the current contract',
    'SENDER': 'SENDER\nSENDER :: A => address : A\nPush the contract that initiated the current internal transaction',
    'SEQ': 'code1 ; code2\ncode1 ; code2 :: A => C\nInstruction sequence',
    'SET_DELEGATE': 'SET_DELEGATE\nSET_DELEGATE :: option key_hash : A => operation : A\nPush a delegation operation',
    'SHA256': 'SHA256\nSHA256 :: bytes : A => bytes : A\nCompute a SHA-256 cryptographic hash',
    'SHA512': 'SHA512\nSHA512 :: bytes : A => bytes : A\nCompute a SHA-512 cryptographic hash',
    'SIZE': 'SIZE\n'
            'SIZE :: set cty : A => nat : A\n'
            'SIZE :: map kty vty : A => nat : A\n'
            'SIZE :: list ty1 : A => nat : A\n'
            'SIZE :: string : A => nat : A\n'
            'SIZE :: bytes : A => nat : A\n'
            'Obtain size of a string, list, set, map or byte sequence',
    'SLICE': 'SLICE\n'
             'SLICE :: nat : nat : string : A => option string : A\n'
             'SLICE :: nat : nat : bytes : A => option bytes : A\n'
             'Obtain a substring or subsequence of a string respectively byte sequence bytes',
    'SOME': 'SOME\nSOME :: ty1 : A => option ty1 : A\nWrap an existing optional value',
    'SOURCE': 'SOURCE\nSOURCE :: A => address : A\nPush the contract that initiated the current transaction',
    'STEPS_TO_QUOTA': '\nPush the remaining steps before the contract execution must terminate',
    'SUB': 'SUB\n'
           'SUB :: nat : nat : A => int : A\n'
           'SUB :: nat : int : A => int : A\n'
           'SUB :: int : nat : A => int : A\n'
           'SUB :: int : int : A => int : A\n'
           'SUB :: timestamp : int : A => timestamp : A\n'
           'SUB :: timestamp : timestamp : A => int : A\n'
           'SUB :: mutez : mutez : A => mutez : A\n'
           'Subtract two numerical values',
    'SWAP': 'SWAP\nSWAP :: ty1 : ty2 : A => ty2 : ty1 : A\nSwap the top two elements of the stack',
    'TOP': '',
    'TRANSFER_TOKENS': 'TRANSFER_TOKENS\n'
                       'TRANSFER_TOKENS :: ty1 : mutez : contract ty1 : A => operation : A\n'
                       'Push a transaction operation',
    'UNIT': 'UNIT\nUNIT :: A => unit : A\nPush the unit value onto the stack',
    'UNPACK': 'UNPACK ty1\nUNPACK ty1 :: bytes : A => option ty1 : A\nDeserialize data, if valid',
    'UPDATE': 'UPDATE\n'
              'UPDATE :: cty : bool : set cty : A => set cty : A\n'
              'UPDATE :: kty : option vty : map kty vty : A => map kty vty : A\n'
              'UPDATE :: kty : option vty : big_map kty vty : A => big_map kty vty : A\n'
              'Add or remove an element in a map, big_map or set',
    'XOR': 'XOR\nXOR :: bool : bool : A => bool : A\nXOR :: nat : nat : A => nat : A\nBoolean and bitwise exclusive OR',
    'address': 'address\nAddress of an untyped contract',
    'big_map': 'big_map kty vty\nA lazily deserialized map from kty to vty',
    'bool': 'bool\nA boolean',
    'bytes': 'bytes\nA sequence of bytes',
    'chain_id': 'chain_id\nA chain identifier',
    'contract': "contract type\nAddress of a contract, where type is the contract's parameter type",
    'int': 'int\nAn arbitrary-precision integer',
    'key': 'key\nA public cryptography key',
    'key_hash': 'key_hash\nA hash of a public cryptography key',
    'lambda': 'lambda ty1 ty2\nA lambda with given parameter and return types',
    'list': 'list type\nA single, immutable, homogeneous linked list',
    'map': 'map kty vty\nAn immutable map from kty to vty',
    'mutez': 'mutez\nA specific type for manipulating tokens',
    'nat': 'nat\nAn arbitrary-precision natural number',
    'operation': 'operation\nAn internal operation emitted by a contract',
    'option': 'option type\nAn optional value',
    'or': 'or ty1 ty2\nA union of two types',
    'pair': 'pair ty1 ty2\nA pair of values',
    'set': 'set cty\nAn immutable set of comparable values of type cty',
    'signature': 'signature\nA cryptographic signature',
    'string': 'string\nA string of characters',
    'timestamp': 'timestamp\nA real-world date',
    'unit': 'unit\nThe type whose only value is Unit'}
