from unittest import TestCase
from pytezos.crypto.hash import (
    operation_list_list_hash,
    block_payload_hash
)

# https://rpc.tzkt.io/mainnet/chains/main/blocks/2223648
operation_hashes_llo = 'LLoaQ8vjCwYooVy6nRSUP9VRBk1YHaHgqWrHw3J9j4VmEvVZCbaYB'
operation_hashes = [
    ["oofVGFJuMPd6XpSvXKRVU6AuE6DtAbBibyfUzXdqfrCDTPuraJQ", "oo8iiB6A3WJBzEwc74jMRtb9gyzbEenKuLLwUFmQ4xS98HyFJTu",
     "ooGn6pyqjMSmjSGRdm2fS8SAzzVh1JEz3qDiviLdHAcKViXWycB", "opFfqxztw69M4m7MPqD63sfZdwF74A8ThDricTQKgiTbNd4ydwc",
     "op5RZXfy4duRbw69qYW99YJvfMCDjyvuDs4s33qjYXBgxmCRp4f", "ooyDEUZAFxEpd2HY9VNb94ahj2HYsLUHCcNYSqKepiP3bw6RpnK",
     "opMe31pUFbaEtD5KJask8Uc8yUZf6anhvNdMG6FYuxmXrnAWSnx", "opF1AskkJxmA8yZ9cSTFFPBSEr4DGS7QTrRxFQtDTyQovqLt1yF",
     "ooA93x3EopoPQXfmqZEMw4SV5rHiLAkLUKWmer2t3bSSKtJMkrj", "ooa9bxcu3KVkz8VL7E3L8iKbacKLFZDDm16QX5q78w6TWqWV1rA",
     "oowjubMor6aVxSALd7cuEQNBmKw44CeqNYqjuQdfQ25conXcddB", "opRiXgV2AHhVKvs3rDG9G4rcPUBDJZxAHz3knbgHWkhxzxunxCV",
     "ooay46SGffH5uDrwTzZncG9ddtCRXWsDTsb5vB9AXZoqkPe1LwJ", "ooVWhZr6MX9mNwMzdDPpf5ymKEvzrCR5aVRVqAk1XDhFSHAWAGG",
     "op116mqfnbSFjutJYKgTutrqTrjDzLTL34RaJ2gfQF6z92B1GEd", "ooJNd7bFHgMxuH2yNJZk5UWAPZQE4Q9rBYnCWg4j2Ew1uBx47Hj",
     "ooxFdyNjjGW3179jxQPjQupFmgAaaYhy5pNFxK2tAwNJoh8ESTD", "ooDPfEsSiicmxWBWZ8r9ZJL2YgFYiE4pFFtJzLtyrF8NCjsQ1xA",
     "opVY4fhUQHSRDMDbfNzEn298cZu9ebb3pT617gDi9KyLcmTg6ET", "ooRQEKVpWAApe6nycqTSu3KUy3ytZvDzfwbWAckqzHaHa663iak",
     "ooHrrz1nuhQnpztLJs89XCAGKTeYYZp7LoumZhbqTrqdxNTuJSX", "onoxNGDu2NBnJxZVMoUhtSqhjsWbEBPaYFneEGTv3DowzDNnxzf",
     "ooziT9HehywMZy7kwEVHsyignQH5MfcdWofoCjBzuX56QnnkrLW", "oodvdNyGYuZvDetJTyrKei6V1VtwUt74bdKrbjAqEyCJ1T5WH6t",
     "opW8MQ94tjkezHMsJ2GSbhLkYrcnVQHB5bPpYouWH2GJcBtbV89", "oo3TMGKAC67bw47dwtKLfPiNtYP9MPAnnuLKbRQNphE1Mtd9ScJ",
     "opMiDtu78kBSWnLBjJRqgH82gt5TNHejvpDXMhqxZ1K9bVwrETd", "ooDM5VKmKF5dLYVeqkhdSN7F3eB4vy3SZu3RWFEPzpyzfgrjrha",
     "opSiekJZ9T7ZErqxANG8dahR79xyXV1f4ikkunv6SaPcHqN2jrt", "opQHcRjqtJcBaqSUTtV5f1rtbwZNy3K8nypSwcVYHG5EyG6ifQD",
     "opHTzUG8nymqCxCh626JBbu8ihdHvapNBGVk4xchYFzMQJDJUq3", "opGrWMeR2brmv8ufXvXDw9sUX2nXRSDGYYwciPcRHHRiQvdDavp",
     "opDxagryp2fbytCz9zDPKXT9XSy19CZopK8wGsGXvE3Fftf2UiU", "oopYPg1PMyRi9ruAH2z1gcxDfMYNLbkSH1F2wb42zF4pMiJpeue",
     "ooTcfv286MjhBEUTHMtRUxQSdtaJ8jMmKqKCX8FVS14KhgShqXu", "ooHZMczKqhMUdgtwSc1xLgN2tQwmhQD3KNVfCdCRuavFJ8Fdmw3",
     "ooEqSoXmyuiXLExrs2yGKaokcP2H6353tyP3KmHdhavuDDnTqbB", "ooBWF9QmkBowBW84UwThBZ2LGWu9p6Yerfh6takdnUpFP7AqYrU",
     "oo8tq9D4Wg6zmL6E9UhhbBVgT13mpJSpf4gwVYVSbYHbV1uRy8N", "oo7ZrkX9ZJcYWC4NisVXHgbKK6ov1aXbQHHfLata27jWrdfJXFX",
     "onzq9eUPiXq35uXch5sa7T1dWaT1iZWjYiNePYVcsJS4WMQBo2h", "onuqm2tjCZWqthQBEi4Y1cVtLwYAr4YaJLU2aYLTcpNjnUgtLYg",
     "onumF5NSwJSFpp2zVyQKq6BWCwmfYnpLWzQEJjLb8bnSqETxwPQ", "onrnSo4UCu7KC93tmfWYeHvmr6xjAYWdUysxDuxd1CwT5bCg9Xg"], [],
    [], ["ooUkXSA4JEBGj3vq8KdoaLXKrGXRDyJuQNjVVacLUMqWMGEzgoD", "onrERtizR9K9BZo5E3XdsJsXTragYfYaLBmMgZ3HrkaU2WpCts5",
         "onpxSxRpTygyLqrAA62PBzZKT14vnsb9GfUY19sNJ5PjruQMzJQ", "op7fZ26fv6bfPPNh51m4vuDJZqsCAh91bJ26huPmZdMugr7dynF",
         "ooZmDSaT8JGLdRNGJqdvE8FC37w4hHQmRD1U4ZbZaZ3hP7j522s", "ooA3srdnj1rsmQogHVyVKu6j2LaWb5dotCcaLW6vvMNLcZ8f88x",
         "oovnjhrHMeMBpkvTHxSNvapV7iQ6hFsSSL6LzmwkHCXatWNFF1q", "opDXgb3ZCM7eH4zkByLbQc3Y3HA7tqgbec2C9sEbjki4dWSkfW3",
         "opaBjse3Y3DzCKUS5bJGDs54HMBtvsKS6DEePWX2mU5keVy8YJk", "oobZRdMm1Ps42zmJRE5h4jaXoEiySrUgExSKe5VZT27w26EY5Zd",
         "ooXuUPBCVwgws7ETBxzYUMjKq3JMamKiiUkoDUHNPmntjzfkwKp", "opBawsSsFxMhR46whEhfNX558vCW4CWc5AddCuNtcyGd8dk9h6F",
         "ood6iz7LVikCx3T6rMviLSNz6oJUxbNGJKFVbHGqiBLN7r87zs8", "onq7Fe3NABrTkb2PZKBvrAefu5J6TxfhJNDCzAGpXc59bCKcEvB",
         "ooHggHarwD3kzuPzt3WWV4PaPjbzh18egp4NR3fJTYYt3vpiw5e", "op4bzVsUnWzsfR3tf7gwETmReqFjPwSbWrAtcJv7z6VaFQadax3",
         "opWc6Zop56wKAqxRR1phvDYqCRQJyZiF9agWnKJ4QsE2cVxjFNe", "oopugtVGMbreEiikGdUrBSkkbdPPuEANorEs89iptxPKiBq8SnV",
         "onksk5ESiNVvrvbXc6xPJhtRKbnXsNJRzteW73cJv7nMCG4kezX", "opWQr3ZpadegC5SUfUw8A8W4p3bQUSX4DS6mygY7FzG9xH5QDgT",
         "ooWbP6PQp1FreE3ikDfTvL9zXVA23A1BKT91RJYYkBEF9nHuYoQ", "onkWcVNEprcxu4dfXJvrPvWPixnTjXkErGA32XnonNVEriskXNC"]]

# https://rpc.tzkt.io/ithacanet/chains/main/blocks/288671
predecessor_1 = 'BL1whyhJA8fUF2ziNZj1MnHFQNLD6QTZTTHiG1oL8LSFwdJQ43z'
block_payload_hash_1 = 'vh29w4KZGVb3A9QyjzDetftoWiCfvRugwAiaQ5Z3FFScy7QzjmH9'
operation_hashes_1 = ["ooa2pnEHguRveoV8WMYswpuSkyvxKTA9hyHDAsVgc9qnXtcDxd7"]

# https://rpc.tzkt.io/ithacanet/chains/main/blocks/10000/header
predecessor_2 = 'BLLiiqQeQ1N35S6VXeNcsyQPphoM17ZCXm9M6ek3xPYXj1tX2pE'
block_payload_hash_2 = 'vh3XZvx7wgTBp92mUVJ9jBNC1NQ79d6DBJm9pappux3exakXJaUU'
operation_hashes_2 = []


class TestHashes(TestCase):

    def test_operation_hash_hash(self):
        res = operation_list_list_hash(operation_hashes)
        self.assertEqual(operation_hashes_llo, res)

    def test_payload_hash_empty(self):
        res = block_payload_hash(
            predecessor=predecessor_2,
            payload_round=0,
            operation_hashes=operation_hashes_2
        )
        self.assertEqual(block_payload_hash_2, res)

    def test_payload_hash_tx(self):
        res = block_payload_hash(
            predecessor=predecessor_1,
            payload_round=0,
            operation_hashes=operation_hashes_1
        )
        self.assertEqual(block_payload_hash_1, res)
