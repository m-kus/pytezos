from pytezos.michelson.micheline import blind_unpack

packed_micheline = '05020000001e070401000000083631363136313631010000000a37333634363436343634'
expected_michelson = '{ Elt "61616161" "7364646464" }'

micheline_bytes = bytes.fromhex(packed_micheline)
michelson = blind_unpack(micheline_bytes)

assert expected_michelson == michelson, (expected_michelson, michelson)
